# MYTHAS - Fiche audit: SWE-bench

## Identite
- **Nom**: SWE-bench
- **Famille**: code / agents
- **Source primaire**: https://arxiv.org/abs/2310.06770 + https://github.com/SWE-bench/SWE-bench
- **Date de creation**: 2023-10

## Acces au test
- **Test public**: oui — prouve
- **Detail acces**: prouve — issues GitHub reelles, repos sources publics, patches de reference, harness d'eval, tout public
- **Mirrors connus**: prouve — HuggingFace (princeton-nlp/SWE-bench), subsets SWE-bench Lite (300 items) et SWE-bench Verified (~500 items valides par humains)

## Setup exact
- **Format**: repo-level software engineering — resoudre une issue GitHub reelle en generant un patch
- **Nombre d'items**: prouve — 2294 items (full), 300 (Lite), ~500 (Verified)
- **Shots**: prouve — 0-shot; le modele recoit l'issue + le repo et doit produire un patch
- **Instructions**: variable — system prompt et scaffolding (agent framework) varient enormement

## Prompt regime
- **Prompt template**: prouve — pas de template unique; chaque agent framework (SWE-agent, Devin, Agentless, etc.) a son propre pipeline
- **CoT**: prouve — la plupart des systemes utilisent du raisonnement iteratif avec tool-use
- **Parsing reponse**: prouve — extraction d'un diff/patch, application au repo, execution des tests
- **Sensibilite prompt mesuree**: a verifier — pas de mesure canonique; mais les variations entre frameworks montrent une forte dependance au scaffolding

## Scoring
- **Metrique**: % d'instances resolues (tests passent apres application du patch)
- **Budget d'echantillonnage**: prouve — certains systemes generent plusieurs patches et selectionnent; le budget de compute (tokens, tentatives, temps) varie enormement
- **Post-processing**: prouve — selection de patch, reruns, filtrage par tests supplementaires

## Version modele
- **Snapshot requis**: plausible — les systemes combinent souvent plusieurs modeles + tooling; la "version" est floue
- **API vs weights**: mixte — API pour les LLMs, tooling custom pour le scaffolding
- **Reproductibilite declaree**: plausible — le harness est public mais les agents frameworks complets sont rarement 100% reproductibles

## Contamination
- **Surface directe**: prouve — les issues, PRs, code source et tests sont des repos GitHub publics; ces repos sont dans les corpus de train de la plupart des LLMs
- **Surface indirecte**: prouve — historique de commits, commentaires, discussions, CI logs: tout est indexe et potentiellement ingere
- **Mesures anti-contamination**: prouve — SWE-bench Verified ajoute une validation humaine des instances mais ne resout pas la contamination du code source sous-jacent
- **Niveau de risque Mythas**: eleve

## Gaming
- **Prompt tuning**: prouve — le scaffolding agent est le principal levier; changer le framework change massivement le score
- **Format fitting**: plausible — certains systemes peuvent sur-optimiser pour le format patch/diff attendu par le harness
- **Hill-climbing**: prouve — SWE-bench est devenu LE benchmark agents; course au leaderboard intense
- **Harness overfitting**: prouve — adapter le framework au harness d'eval (retry, selection, tests supplementaires) gonfle le score sans ameliorer la capacite reelle
- **Niveau de risque Mythas**: critique

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: inutilisable (re-audit v0.5, 2026-04-19)
- **Verdict anterieur**: fragile (2026-04-19, pre-seuils v0.5)
- **Resume**: Benchmark realiste mais contamination structurelle par repos GitHub publics et scaffolding-dependent. Sous v0.5, 5 zeros + s=1 => inutilisable. Realisme n'equivaut pas a Mythas-compatibilite.
- **Date audit**: 2026-04-19

## Verdict v0.5 (re-audit 2026-04-19)
- **closure**: 0 (prouve) - issues, repos et patches de reference publics
- **contamination_direct**: 0 (prouve) - repos sources dans les corpus de train, contamination structurelle non eliminable
- **contamination_indirect**: 0 (prouve) - PRs, commentaires, tests, historique commits tous indexes
- **incomparability**: 0 (prouve) - score depend autant du framework agent que du modele; aucun scaffolding canonique
- **gaming_surface**: 0 (prouve) - 4+ categories (prompt_tuning, harness_overfitting, hill_climbing, protocol_fragmentation)
- **governance**: 1 (plausible) - `SWE-bench Verified` = curation tierce one-shot, pas de mecanisme continu
- **s**: 1, **zeros**: 5
- **Verdict derive**: inutilisable (regle `zeros >= 5`)
- **Reclassement**: fragile -> inutilisable
