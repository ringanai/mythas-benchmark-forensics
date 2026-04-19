# MYTHAS - Fiche audit: HumanEval

## Identite
- **Nom**: HumanEval
- **Famille**: code
- **Source primaire**: https://arxiv.org/abs/2107.03374 + https://github.com/openai/human-eval
- **Date de creation**: 2021-07

## Acces au test
- **Test public**: oui — prouve
- **Detail acces**: prouve — 164 problemes avec docstrings, signatures et tests unitaires, tout public sur GitHub
- **Mirrors connus**: prouve — HuggingFace (openai/humaneval), forks GitHub, blogs avec solutions completes, datasets derives (HumanEval+, EvalPlus)

## Setup exact
- **Format**: code generation — completer une fonction Python a partir de docstring + signature
- **Nombre d'items**: prouve — 164 problemes
- **Shots**: prouve — 0-shot (generation directe a partir du prompt)
- **Instructions**: prouve — prompt = docstring + signature, pas de system prompt prescrit

## Prompt regime
- **Prompt template**: prouve — le prompt est la docstring elle-meme; pas de template externe impose
- **CoT**: variable — certains evaluent avec raisonnement, d'autres en generation directe
- **Parsing reponse**: prouve — extraction du code genere, execution contre tests unitaires
- **Sensibilite prompt mesuree**: a verifier — pas de mesure canonique de prompt sensitivity dans la source primaire

## Scoring
- **Metrique**: pass@k (k=1, 10, 100 dans le papier original)
- **Budget d'echantillonnage**: prouve — pass@k depend directement du nombre de samples generes; plus de samples = score plus eleve mecaniquement
- **Post-processing**: prouve — selection parmi n samples, execution des tests, calcul pass@k avec estimateur non-biaise

## Version modele
- **Snapshot requis**: non — rarement specifie dans les comparaisons publiques
- **API vs weights**: mixte
- **Reproductibilite declaree**: plausible — le benchmark est simple a lancer mais pass@k, temperature, nombre de samples et timeout rendent les comparaisons fragiles

## Contamination
- **Surface directe**: prouve — 164 problemes publics depuis 2021, solutions omnipresentes sur GitHub, blogs, Stack Overflow
- **Surface indirecte**: prouve — les problemes sont simples et proches de exercices de coding courants; overlap avec corpus de train quasi-garanti
- **Mesures anti-contamination**: aucune — benchmark statique public
- **Niveau de risque Mythas**: critique

## Gaming
- **Prompt tuning**: plausible — adapter le prompt autour de la docstring peut changer le taux de reussite
- **Format fitting**: prouve — les 164 problemes sont simples et memorisables; un modele peut les "connaitre" sans generaliser
- **Hill-climbing**: prouve — benchmark central dans le marketing "code generation", forte incitation a optimiser
- **Harness overfitting**: prouve — pass@k est gonflable par budget d'echantillonnage; pass@1 vs pass@100 racontent des histoires tres differentes
- **Niveau de risque Mythas**: critique

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: inutilisable (re-audit v0.5, 2026-04-19)
- **Verdict anterieur**: compromis (2026-04-19, pre-seuils v0.5)
- **Resume**: 164 problemes simples et publics depuis 2021; contamination quasi-certaine, pass@k gonflable. Sous les seuils v0.5, toutes dimensions a 0 => inutilisable.
- **Date audit**: 2026-04-19

## Verdict v0.5 (re-audit 2026-04-19)
- **closure**: 0 (prouve) - 164 problemes publics depuis 2021, solutions omnipresentes
- **contamination_direct**: 0 (prouve) - mirroring quasi-universel, aucune decontamination
- **contamination_indirect**: 0 (prouve) - solutions detaillees, blogs, repos tiers, distillations
- **incomparability**: 0 (prouve) - temperature, samples, timeout, pass@k divergents sans consensus
- **gaming_surface**: 0 (prouve) - 4+ categories (prompt_tuning, format_fitting, harness_overfitting, hill_climbing)
- **governance**: 0 (prouve) - publie 2021, laisse en l'etat, aucune gouvernance continue
- **s**: 0, **zeros**: 6
- **Verdict derive**: inutilisable
- **Reclassement**: compromis -> inutilisable
