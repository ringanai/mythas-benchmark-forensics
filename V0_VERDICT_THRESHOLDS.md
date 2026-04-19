# MYTHAS - Seuils de verdict v0.5

## But

Jusqu'ici, les verdicts `fiable` / `fragile` / `compromis` / `inutilisable` ont ete attribues benchmark par benchmark sur la base du jugement methodologique de l'auditeur, en s'appuyant sur la taxonomie (`BENCHMARK_GAMING_TAXONOMY.md`) et la spec (`ANTI_LIE_BENCH_V0.md`).

Ce document formalise ces seuils pour qu'un verdict devienne derivable a partir d'un ensemble borne de dimensions observables, au lieu de rester un pur arbitrage humain.

La version est `v0.5`. Les seuils sont maintenant encodes dans `V0_FICHE_SCHEMA.json` via un bloc optionnel `verdict`, et verifies semantiquement par `validate_v0_fiche.py`.

---

## 1. Les 4 verdicts Mythas

- **fiable**
  - le benchmark peut servir d'ancre de reference pour une fiche Mythas `ancrage fort`
  - un score publie dessus est interpretable si la fiche v0 est complete

- **fragile**
  - le benchmark peut servir de borne publique de competence, preference ou scaffolding
  - un score publie dessus n'est pas une ancre anti-lie mais reste publiable en statut `borne publique`

- **compromis**
  - le benchmark souffre d'au moins une atteinte severe (contamination directe, non-comparabilite documentee, gaming structurel)
  - un score publie dessus ne peut etre endosse que comme curiosite historique, jamais comme mesure de capacite actuelle

- **inutilisable**
  - le benchmark accumule plusieurs atteintes severes sans mitigation documentee
  - aucun score publie dessus n'est Mythas-compatible, quelle que soit la qualite de la fiche

---

## 2. Dimensions d'evaluation

Un verdict est derive de 6 dimensions observables. Chaque dimension est notee sur 3 niveaux: `0` (rouge), `1` (jaune), `2` (vert). Chaque note est marquee `prouve` / `plausible` / `a verifier`.

### 2.1 Fermeture du test (`closure`)

- `2` - test ferme, items et labels non distribues, mecanisme d'evaluation tiers documente
- `1` - test partiellement ferme (release tournante, separation temporelle stricte, hold-out controle)
- `0` - test entierement public, items et labels accessibles sans friction

### 2.2 Contamination directe (`contamination_direct`)

- `2` - contamination directe mesuree et rapportee comme marginale, ou structurellement impossible (test ferme ou pre-cutoff)
- `1` - contamination directe mitigee (decontamination explicite, release recente, separation temporelle) mais non mesuree chiffree
- `0` - contamination directe probable ou quasi-certaine (items publics depuis des annees, miroirs multiples, pas de mitigation)

### 2.3 Contamination indirecte (`contamination_indirect`)

- `2` - pas de surface indirecte connue (pas de solutions publiees, pas de walkthroughs, pas de repos derivatifs largement indexes)
- `1` - surface indirecte existante mais contenue (quelques ressources tierces, pas de saturation web)
- `0` - surface indirecte massive (solutions detaillees, blogs, repos, distillations, socratic variants, datasets miroirs)

### 2.4 Non-comparabilite documentee (`incomparability`)

- `2` - protocole canonique unique, harness figé publiquement, parser et scoring reproductibles
- `1` - plusieurs harnesses co-existent, mais les ecarts sont documentes et le protocole dominant est identifiable
- `0` - implementations multiples produisent des chiffres non-comparables et parfois des classements differents, sans consensus methodologique

### 2.5 Surface de gaming structurelle (`gaming_surface`)

Nombre de categories de la taxonomie Mythas (`BENCHMARK_GAMING_TAXONOMY.md`) auxquelles le benchmark est structurellement expose, hors contamination directe (`contamination_direct`) deja notee separement. Categories considerees ici: contamination_indirecte, prompt_tuning, format_fitting, hill_climbing_leaderboard, harness_overfitting, style_gaming_judge_gaming, protocol_fragmentation.

- `2` - 0 ou 1 categorie applicable
- `1` - 2 ou 3 categories applicables
- `0` - 4 categories ou plus applicables

### 2.6 Gouvernance anti-gaming (`governance`)

- `2` - mecanisme de soumission tierce, re-release reguliere, separation temporelle systematique, ou equivalent documente
- `1` - mitigation partielle: decontamination one-shot, versioning public, mais pas de mecanisme continu
- `0` - aucune gouvernance anti-gaming documentee; le benchmark est publie et laisse en l'etat

---

## 3. Matrice de passage verdict

Soit `s = closure + contamination_direct + contamination_indirect + incomparability + gaming_surface + governance` (score maximal = 12).

Soit `zeros = nombre de dimensions notees 0`.

- **fiable**
  - `closure >= 1`
  - `contamination_direct >= 2`
  - `governance >= 1`
  - `s >= 9`
  - `zeros == 0`

- **fragile**
  - ne satisfait pas `fiable`
  - `zeros <= 2`
  - `s >= 5`
  - au moins une dimension n'est pas `2` ou `closure == 0` ou `governance == 0`

- **compromis**
  - ne satisfait pas `fragile`
  - `s >= 2`
  - `zeros <= 4`

- **inutilisable**
  - `zeros >= 5`
  - ou `s < 2`

**Regles de sortie (dures):**

- si `contamination_direct == 0` et `contamination_indirect == 0` et `governance == 0`, le verdict est au mieux `compromis`
- si `contamination_direct == 0` et `closure == 0`, le verdict est au mieux `compromis`
- une dimension notee `a verifier` sans valeur de repli degrade automatiquement d'un niveau vers `fragile` ou `compromis` selon le cas, pour respecter le principe "absence de preuve n'est pas preuve d'absence"

---

## 4. Retro-application aux fiches deja auditees

Application informelle des seuils aux verdicts deja poses dans `OUTBOX.md` (toutes dimensions sont `plausible` sauf marquage explicite; cette section est une sanity check, pas un re-audit complet).

| Benchmark | closure | cont_dir | cont_ind | incomp | gaming | gouv | s | zeros | verdict derive | verdict actuel |
|---|---|---|---|---|---|---|---|---|---|---|
| MMLU | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 5 | inutilisable | compromis |
| MMLU-Pro | 0 | 1 | 1 | 1 | 1 | 1 | 5 | 1 | fragile | fragile |
| MMLU-CF | 2 | 2 | 1 | 1 | 2 | 1 | 9 | 0 | fiable | fiable |
| HELM MMLU | 0 | 0 | 0 | 2 | 1 | 0 | 3 | 4 | compromis | fragile |
| GSM8K | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 4 | compromis | fragile |
| MATH | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 4 | compromis | compromis |
| HumanEval | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 5 | inutilisable | compromis |
| MBPP | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 4 | compromis | compromis |
| SWE-bench | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | inutilisable | fragile |
| LiveBench | 1 | 1 | 1 | 1 | 1 | 1 | 6 | 0 | fragile | fragile |
| LiveCodeBench | 1 | 1 | 1 | 1 | 1 | 1 | 6 | 0 | fragile | fragile |
| BigCodeBench | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 5 | inutilisable | fragile |
| Chatbot Arena | 0 | 1 | 1 | 0 | 0 | 1 | 3 | 3 | compromis | fragile |
| Open LLM Leaderboard archive | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 5 | inutilisable | fragile |

Lecture:
- `prouve` - MMLU-CF sort bien `fiable` sous ces seuils, coherent avec le verdict existant
- `prouve` - LiveBench et LiveCodeBench sortent `fragile`, coherent
- `a verifier` - MMLU, HumanEval, SWE-bench, BigCodeBench, Open LLM Leaderboard sortent plus durs que le verdict actuel (`inutilisable` vs `compromis` ou `fragile`)
- `plausible` - l'ecart n'est pas force un bug des seuils: il reflete le fait que les verdicts actuels ont ete attribues avant que les regles de sortie dures et la dimension `governance` soient formalisees
- `a verifier` - les notes par dimension ci-dessus sont une estimation rapide; un vrai re-audit doit les confirmer fiche par fiche

---

## 5. Ce que les seuils ferment

- `prouve` - un verdict Mythas devient derivable a partir de 6 notes 0/1/2, pas d'une impression globale
- `prouve` - `fiable` est dur a atteindre: il exige simultanement fermeture, gouvernance, contamination directe mesuree, aucune dimension a 0
- `prouve` - un benchmark purement public avec contamination directe probable ne peut plus glisser en `fragile` par simple formulation prudente: les regles de sortie le bloquent a `compromis` au mieux
- `prouve` - l'etat `inutilisable` devient atteignable, ce qui evite le plancher implicite `compromis` qui camouflait des cas ou presque rien n'est evaluable

---

## 6. Ce que les seuils ne tranchent pas encore (v0.6)

- `a verifier` - re-audit dimension par dimension de chaque fiche existante dans `fiches/*.md`, avec evidence chiffree quand disponible
- `prouve` - encodage machine minimal en place: `verdict.dimensions` + `verdict.derived_verdict` dans `V0_FICHE_SCHEMA.json`, derive semantique dans `validate_v0_fiche.py`, avec fixtures de regression
- `a verifier` - poids relatifs: les seuils actuels traitent toutes les dimensions avec le meme poids; un poids plus eleve pour `closure` et `contamination_direct` serait defendable mais n'est pas encore instrumente
- `a verifier` - traitement des benchmarks hybrides (dynamique + leaderboard + judge): faut-il une note `gaming_surface` distincte par signal mesure
- `a verifier` - cadence de re-audit temporel: les notes de contamination et de gouvernance ne sont pas statiques

---

## 7. Refus explicites

- `prouve` - un verdict fiable ne peut pas etre atteint sans `closure >= 1` et `governance >= 1`: un benchmark purement public sans gouvernance ne devient jamais ancre anti-lie, quelle que soit la qualite du reste
- `prouve` - un score `ancrage fort` publie sur un benchmark que les seuils classent `fragile` ou pire est refuse: l'ancrage d'une fiche ne peut pas depasser le verdict du benchmark qu'elle mesure
- `prouve` - ces seuils ne servent pas a ranger un classement de "meilleurs benchmarks"; ils servent a refuser de traiter un benchmark comme plus solide qu'il ne l'est
