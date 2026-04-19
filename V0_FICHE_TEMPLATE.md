# MYTHAS - Template fiche v0 exportable

Template markdown portable pour publier un score sous label Mythas v0.
Derive de `ANTI_LIE_BENCH_V0.md` section 5, et integre les 3 enseignements des pilotes `fiches/v0-pilot-MMLU-CF.md` et `fiches/v0-pilot-LiveCodeBench.md`:

1. statut de fiche `public-only benchmark` vs `benchmark a test ferme` vs `pilote sans run` (au-dessus du statut `score v0 publie`)
2. gabarit d'axes de comparabilite par famille de benchmark (MCQ / math verifiable / code statique / code dynamique / scaffolding agent / arena preference / leaderboard statique)
3. regle formelle de reclassement competence -> scaffolding des que retry, feedback, multi-turn ou outils sont actifs

Chaque champ est marque `prouve` / `plausible` / `a verifier`.
Une fiche incomplete reste `a verifier`, jamais `prouve`.
Une absence de fiche = score non publie.

---

## 0. Statut de fiche

- **Type de fiche** (choisir un seul, obligatoire):
  - [ ] `pilote sans run` — applique la spec v0 sur un benchmark sans produire de score
  - [ ] `score v0 publie, public-only` — benchmark sans test ferme; publiable comme borne publique de competence
  - [ ] `score v0 publie, ancrage fort` — benchmark avec test ferme + mecanisme d'evaluation tiers
  - [ ] `score v0 refuse` — le benchmark ou le protocole echoue une des 6 conditions de section 4 de la spec

- **Niveau d'ancrage anti-lie**: `ancrage fort` | `borne publique` | `hors ancrage`
- **Justification du statut**: 1 a 3 lignes

---

## 1. Identite score

- Benchmark (nom): `...`
- Version / release: `...`
- Subset / split: `...`
- Hash ou identifiant stable du set: `...`
- Fenetre temporelle si applicable (`start_date` / `end_date`): `...`
- Date du run: `...`
- Operateur du run: `...`

## 2. Cible mesuree

- Signal principal (un seul): `competence` | `preference` | `scaffolding`
- Signaux explicitement exclus: `...`
- **Regle de reclassement retry/agent** (obligatoire si applicable):
  - si retry / feedback / multi-turn / outils / self-repair / best-of-n avec verifier actif => le signal ne peut plus etre `competence`
  - reclasser en `scaffolding` et publier la description du scaffold
  - `competence` n'est conservable que sous regime single-shot, sans outils externes, sans retry conditionnel

## 3. Modele

- Nom: `...`
- Snapshot / revision / hash: `...`
- Mode d'acces: `weights` | `API`
- Pour une API: date + revision + region si documentee
- Interdit: "dernier modele proprietaire" ou equivalent non identifiable

## 4. Harness

- Version: `...`
- Hash du code d'eval: `...`
- Backend d'execution: `...`
- Timeouts / retries / batch: `...`

## 5. Prompt regime

- Template exact ou declaration `no template`: `...`
- Shots: `...`
- CoT status: `on` | `off` | `forced` | `free`
- System prompt: `...`
- Ordre des choix / randomization: `...`
- Sensibilite au prompt: `mesuree (valeur)` | `declaree non mesuree`

## 6. Scoring

- Metrique: `...`
- Parser final: `...`
- Post-processing: `...`
- Budget sampling (temperature, top-p, seed, n samples): `...`
- Politique de selection: `greedy` | `majority` | `pass@k` | `best-of-n` | `autre`

## 7. Contamination declaree

- Surfaces directes connues: `...`
- Surfaces indirectes connues: `...`
- Mesures appliquees: `test ferme` | `separation temporelle` | `randomization` | `decontamination` | `aucune`
- Rappel: absence de preuve de contamination n'est pas preuve d'absence

## 8. Gaming declare

- Categories Mythas applicables (cocher, ref `BENCHMARK_GAMING_TAXONOMY.md`):
  - [ ] contamination directe
  - [ ] contamination indirecte
  - [ ] prompt tuning
  - [ ] format fitting
  - [ ] hill-climbing leaderboard
  - [ ] harness overfitting
  - [ ] style gaming / judge gaming
  - [ ] protocol fragmentation
- Mesures anti-gaming en place: `...`

## 9. Bornes de comparabilite

- Comparable avec: `...` (meme benchmark + meme release + meme prompt regime + meme snapshot modele + meme harness + meme budget)
- Non comparable avec: `...`

### 9.bis Axes de comparabilite par famille

Selectionner le gabarit qui correspond a la famille du benchmark.
Un axe non fixe = score non comparable sur cet axe.

- **Famille MCQ / knowledge** (ex: MMLU, MMLU-Pro, MMLU-CF)
  axes: release, subset, prompt template, shots, CoT, ordre des choix, snapshot modele

- **Famille math verifiable** (ex: GSM8K, MATH)
  axes: release, parser final, CoT, self-consistency, budget sampling, calculator/tool usage, snapshot modele

- **Famille code statique** (ex: HumanEval, MBPP)
  axes: release, subset (full vs sanitized), temperature, n samples, pass@k, timeout, snapshot modele

- **Famille code dynamique** (ex: LiveBench, LiveCodeBench, BigCodeBench)
  axes: release, scenario, fenetre temporelle (`start_date` / `end_date`), checker, backend d'execution, harness, prompt regime, budget, snapshot modele

- **Famille scaffolding agent** (ex: SWE-bench)
  axes: release/subset, framework agent, retry policy, tool set, patch selection, tests supplementaires, snapshot modele, scaffold hash
  (signal principal obligatoire: `scaffolding`, jamais `competence`)

- **Famille arena preference** (ex: Chatbot Arena)
  axes: periode, mix de prompts, population votants, metrique (Elo / BT-MLE), anonymisation, snapshot modele
  (signal principal obligatoire: `preference`, jamais `competence`)

- **Famille leaderboard statique** (ex: Open LLM Leaderboard archive)
  axes: version du leaderboard, batterie exacte, harness (lm-eval-harness version), normalisation, snapshot modele

## 10. Statut public / ferme

- Quoi est publie: `schema tache` | `set validation` | `code eval` | `taxonomie gaming` | `fiche` | `autre`
- Quoi est ferme: `test set` | `parsers canoniques` | `seeds` | `scores par item` | `aucune fermeture`
- Mecanisme d'evaluation tiers: `submission protocol` | `validateur externe` | `hold-out controle` | `aucun`
- Si `aucun` et pretention d'ancrage fort => la fiche doit etre reclassee `public-only` ou `refuse`

---

## Regles de sortie

- une fiche qui manque une des 6 conditions de section 4 de la spec n'est pas publiee comme score v0
- une fiche sans statut en section 0 est invalide
- une fiche `score v0 publie, ancrage fort` sans mecanisme d'evaluation tiers (section 10) est invalide
- une fiche `competence` avec retry / feedback / multi-turn / outils / agent actifs est invalide: reclasser `scaffolding`
- une fiche sans axes de comparabilite fixes sur la famille correspondante (section 9.bis) reste `a verifier` sur la comparabilite

## Forme du score publie

Score v0 = triplet + fiche.

- triplet: `(signal, valeur, regime)`
- fiche: sections 0 a 10 completes
- exemple: `(competence, exact_match = 0.742, regime = "MMLU-CF test_ferme_v1 / harness hash X / 5-shot / CoT off / snapshot 2026-03-12")`
