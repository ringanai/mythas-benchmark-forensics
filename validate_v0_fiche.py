import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


DEFAULT_SCHEMA_PATH = Path(__file__).with_name("V0_FICHE_SCHEMA.json")
VERDICT_DIMENSIONS = [
    "closure",
    "contamination_direct",
    "contamination_indirect",
    "incomparability",
    "gaming_surface",
    "governance",
]
VERDICT_RANK = {
    "inutilisable": 0,
    "compromis": 1,
    "fragile": 2,
    "fiable": 3,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def format_path(parts: list[Any]) -> str:
    if not parts:
        return "$"

    chunks: list[str] = ["$"]
    for part in parts:
        if isinstance(part, int):
            chunks.append(f"[{part}]")
        else:
            chunks.append(f".{part}")
    return "".join(chunks)


def degrade_verdict(verdict: str) -> str:
    if verdict == "fiable":
        return "fragile"
    if verdict == "fragile":
        return "compromis"
    return verdict


def cap_verdict(verdict: str, cap: str) -> str:
    if VERDICT_RANK[verdict] > VERDICT_RANK[cap]:
        return cap
    return verdict


def derive_verdict(instance: dict[str, Any]) -> str | None:
    verdict = instance.get("verdict")
    if not verdict:
        return None

    dimensions = verdict.get("dimensions", {})
    scores = {
        name: dimensions[name]["score"]
        for name in VERDICT_DIMENSIONS
    }
    evidences = {
        name: dimensions[name]["evidence"]
        for name in VERDICT_DIMENSIONS
    }

    total = sum(scores.values())
    zeros = sum(1 for value in scores.values() if value == 0)

    if (
        scores["closure"] >= 1
        and scores["contamination_direct"] >= 2
        and scores["governance"] >= 1
        and total >= 9
        and zeros == 0
    ):
        derived = "fiable"
    elif zeros >= 5 or total < 2:
        derived = "inutilisable"
    elif zeros <= 2 and total >= 5:
        derived = "fragile"
    elif total >= 2 and zeros <= 4:
        derived = "compromis"
    else:
        derived = "inutilisable"

    if (
        scores["contamination_direct"] == 0
        and scores["contamination_indirect"] == 0
        and scores["governance"] == 0
    ):
        derived = cap_verdict(derived, "compromis")

    if scores["contamination_direct"] == 0 and scores["closure"] == 0:
        derived = cap_verdict(derived, "compromis")

    if any(evidence == "a verifier" for evidence in evidences.values()):
        derived = degrade_verdict(derived)

    return derived


def semantic_verdict_errors(instance: dict[str, Any]) -> list[dict[str, Any]]:
    verdict = instance.get("verdict")
    if not verdict:
        return []

    expected = derive_verdict(instance)
    actual = verdict.get("derived_verdict")
    errors: list[dict[str, Any]] = []

    if expected is not None and actual != expected:
        errors.append(
            {
                "kind": "semantic_error",
                "message": f"derived_verdict should be '{expected}', got '{actual}'",
                "path": "$.verdict.derived_verdict",
                "schema_path": "$.verdict.derived_verdict",
            }
        )

    status = instance.get("status", {})
    fiche_type = status.get("fiche_type")
    anchor_level = status.get("anchor_level")
    if (
        fiche_type in {"score v0 publie, public-only", "score v0 publie, ancrage fort"}
        and anchor_level == "ancrage fort"
        and expected is not None
        and expected != "fiable"
    ):
        errors.append(
            {
                "kind": "semantic_error",
                "message": (
                    "a published fiche cannot claim anchor_level='ancrage fort' "
                    f"when verdict derives to '{expected}'"
                ),
                "path": "$.status.anchor_level",
                "schema_path": "$.verdict.derived_verdict",
            }
        )

    if (
        expected == "inutilisable"
        and anchor_level is not None
        and anchor_level not in {"hors ancrage", "borne publique"}
    ):
        errors.append(
            {
                "kind": "semantic_error",
                "message": (
                    "derived_verdict='inutilisable' restricts anchor_level to "
                    f"{{'hors ancrage','borne publique'}}, got '{anchor_level}'"
                ),
                "path": "$.status.anchor_level",
                "schema_path": "$.verdict.derived_verdict",
            }
        )

    return errors


def validate_instance(validator: Draft202012Validator, path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "file": str(path),
        "valid": False,
        "error_count": 0,
        "errors": [],
    }

    try:
        instance = load_json(path)
    except Exception as exc:  # pragma: no cover - defensive CLI branch
        result["errors"] = [
            {
                "kind": "parse_error",
                "message": str(exc),
            }
        ]
        result["error_count"] = 1
        return result

    schema_errors = sorted(validator.iter_errors(instance), key=lambda err: list(err.absolute_path))
    formatted_errors = [
        {
            "kind": "validation_error",
            "message": error.message,
            "path": format_path(list(error.absolute_path)),
            "schema_path": format_path(list(error.absolute_schema_path)),
        }
        for error in schema_errors
    ]

    if not schema_errors:
        formatted_errors.extend(semantic_verdict_errors(instance))

    result["valid"] = not formatted_errors
    result["error_count"] = len(formatted_errors)
    result["errors"] = formatted_errors
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Mythas v0 fiche JSON instances against V0_FICHE_SCHEMA.json."
    )
    parser.add_argument("paths", nargs="*", help="JSON fiche path(s) to validate.")
    parser.add_argument(
        "--schema",
        default=str(DEFAULT_SCHEMA_PATH),
        help="Path to the JSON Schema file. Defaults to V0_FICHE_SCHEMA.json next to this script.",
    )
    parser.add_argument(
        "--check-schema",
        action="store_true",
        help="Validate the JSON Schema itself before validating instances.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON output instead of human-readable text.",
    )
    args = parser.parse_args()

    schema_path = Path(args.schema).resolve()
    schema = load_json(schema_path)

    if args.check_schema:
        Draft202012Validator.check_schema(schema)

    if not args.paths:
        payload = {
            "schema": str(schema_path),
            "schema_valid": True,
            "results": [],
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"SCHEMA_OK {schema_path}")
        return 0

    validator = Draft202012Validator(schema)
    results = [validate_instance(validator, Path(path).resolve()) for path in args.paths]
    all_valid = all(item["valid"] for item in results)

    if args.json:
        print(
            json.dumps(
                {
                    "schema": str(schema_path),
                    "schema_valid": True,
                    "results": results,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for item in results:
            print(f"{'VALID' if item['valid'] else 'INVALID'} {item['file']}")
            for error in item["errors"]:
                path_label = error.get("path", "$")
                print(f"  - {path_label}: {error['message']}")

    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
