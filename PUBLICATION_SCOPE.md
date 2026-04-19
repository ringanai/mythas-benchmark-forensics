# MYTHAS - Publication Scope

Ce repo public sert a exposer:

- comment les benchmarks publics peuvent mentir
- comment les scores publics peuvent etre mal interpretes
- comment exprimer une critique benchmark de facon plus rigoureuse

Ce repo ne sert pas a exposer:

- un corpus prive non publie
- des recettes de score inflation
- des tactiques de train on test
- des bridges ops internes
- des loops agentiques locales
- des details de runtime ou d'acces machine

## Ce qui peut etre public

- `README.md`
- `PROJECT_COCKPIT.md`
- `ANTI_LIE_BENCH_V0.md`
- `BENCHMARK_GAMING_TAXONOMY.md`
- `V0_VERDICT_THRESHOLDS.md`
- `V0_FICHE_SCHEMA.json`
- `validate_v0_fiche.py`
- `fiches/*.md`
- `fiches/json/*.json`
- `fiches/json/fixtures/*.json`

## Ce qui reste hors publication

- `INBOX.md`
- `OUTBOX.md`
- `WORKLOG.md`
- `SOURCE_INBOX.md`
- prompts Claude / Codex
- scripts H24
- ponts distants
- corpus proprietaires
- runs prives

## Regle editoriale

Si un fichier aide a comprendre:

- comment critiquer un benchmark
- comment qualifier un verdict
- comment verifier la coherence d'une fiche

alors il peut etre publie.

Si un fichier aide surtout a:

- operer les agents
- orchestrer les machines
- proteger un corpus prive
- ou faire monter artificiellement un score

alors il ne doit pas etre publie.
