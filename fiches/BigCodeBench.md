# MYTHAS - Fiche audit: BigCodeBench

## Identite
- **Nom**: BigCodeBench
- **Famille**: code
- **Source primaire**: https://arxiv.org/abs/2406.15877 + https://github.com/bigcode-project/bigcodebench
- **Date de creation**: 2024-06

## Acces au test
- **Test public**: oui - prouve
- **Detail acces**: prouve - taches, evaluateur, leaderboard, releases et samples generes par LLM sont publics; l'execution peut passer par backends distants ou locaux
- **Mirrors connus**: prouve - HuggingFace dataset / collection / leaderboard / evaluator space, releases GitHub, repo d'annotation

## Setup exact
- **Format**: code generation fonctionnel, oriente taches pratiques, avec instructions complexes et diverse function calls
- **Nombre d'items**: prouve - 1140 taches dans BigCodeBench; subset `Hard` de 148 taches
- **Shots**: a verifier - la source primaire documente surtout des generations directes et des modes base/chat, sans regime few-shot canonique unique
- **Instructions**: prouve - deux splits `Complete` et `Instruct`; prompts differencies pour base models et chat models

## Prompt regime
- **Prompt template**: prouve - prompts differents pour base et chat, avec `--direct_completion` necessaire dans certains cas pour eviter un mode chat parasite
- **CoT**: a verifier - pas de regime CoT canonique explicitement documente dans les sources primaires consultees
- **Parsing reponse**: prouve - execution automatisee et calcul de `pass@k` via evaluateur dedie
- **Sensibilite prompt mesuree**: a verifier - pas de mesure canonique unique de prompt sensitivity trouvee dans les sources primaires consultees

## Scoring
- **Metrique**: prouve - `pass@k`
- **Budget d'echantillonnage**: prouve - backend, batch size, temperature, nombre d'echantillons et mode d'execution changent les resultats; le README recommande `--bs 1` pour un greedy plus deterministe
- **Post-processing**: prouve - fichiers `sanitized_calibrated`, reuse de samples pre-generes, execution via `gradio`, `e2b` ou local

## Version modele
- **Snapshot requis**: plausible - les resultats du leaderboard dependent du modele, de sa revision et du backend exact d'execution
- **API vs weights**: mixte - prouve - open weights via HF / vLLM et APIs diverses (OpenAI, Anthropic, Google, Mistral) sont supportees
- **Reproductibilite declaree**: plausible - evaluateur public et session d'execution visible ameliorent l'auditabilite, mais les backends distants et leur variabilite limitent la reproductibilite stricte

## Contamination
- **Surface directe**: plausible - benchmark plus recent et plus difficile que HumanEval, mais entierement public des son lancement
- **Surface indirecte**: prouve - leaderboard, samples generes publics, releases et docs d'eval ajoutent une grosse surface secondaire
- **Mesures anti-contamination**: prouve - aucune mesure forte de test ferme ou de separation temporelle explicite dans les sources primaires consultees
- **Niveau de risque Mythas**: eleve

## Gaming
- **Prompt tuning**: prouve - la distinction base/chat et le flag `--direct_completion` montrent que le mode de prompting influence directement le score
- **Format fitting**: plausible - les splits `Complete` / `Instruct` et l'interface publique de l'evaluateur invitent un fitting benchmark-specifique
- **Hill-climbing**: prouve - leaderboard publique, releases frequentes et samples ouverts encouragent l'optimisation iterative
- **Harness overfitting**: prouve - choix du backend, batch size, execution API et details de l'evaluateur peuvent devenir la vraie cible d'optimisation
- **Niveau de risque Mythas**: eleve

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: compromis (re-audit v0.5, 2026-04-19)
- **Verdict anterieur**: fragile (2026-04-19, pre-seuils v0.5)
- **Resume**: Plus realiste que HumanEval mais pas contamination-safe. Sous v0.5, s=2 avec 2 dimensions a 1 (contamination_indirect, incomparability documentee) => compromis, pas inutilisable.
- **Date audit**: 2026-04-19

## Verdict v0.5 (re-audit 2026-04-19)
- **closure**: 0 (prouve) - tasks, evaluator, leaderboard et samples pre-generes publics
- **contamination_direct**: 0 (plausible) - dataset public des publication, pas de decontamination chiffree
- **contamination_indirect**: 1 (plausible) - plus recent et plus niche que HumanEval/MBPP, surface tierce limitee
- **incomparability**: 1 (prouve) - splits `Complete`/`Instruct`, subsets `Full`/`Hard`, backends varient mais documentes
- **gaming_surface**: 0 (prouve) - 4+ categories (prompt_tuning, format_fitting, harness_overfitting, hill_climbing)
- **governance**: 0 (prouve) - publication one-shot, pas de rotation ni soumission tierce
- **s**: 2, **zeros**: 4
- **Verdict derive**: compromis
- **Reclassement**: fragile -> compromis
