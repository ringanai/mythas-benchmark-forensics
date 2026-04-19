# MYTHAS - Fiche audit: MBPP

## Identite
- **Nom**: MBPP (Mostly Basic Python Programming)
- **Famille**: code
- **Source primaire**: https://arxiv.org/abs/2108.07732 + https://github.com/google-research/google-research/tree/master/mbpp
- **Date de creation**: 2021-08

## Acces au test
- **Test public**: oui — prouve
- **Detail acces**: prouve — ~974 problemes avec enonces en langage naturel, solutions de reference et tests, tout public
- **Mirrors connus**: prouve — HuggingFace (google-research-datasets/mbpp), forks GitHub, subsets sanitized (MBPP-sanitized ~427 items)

## Setup exact
- **Format**: code generation — ecrire une fonction Python a partir d'un enonce en langage naturel + tests d'assertion
- **Nombre d'items**: prouve — 974 total, dont ~427 dans le subset sanitized couramment utilise
- **Shots**: variable — 0-shot et 3-shot selon les implementations
- **Instructions**: prouve — prompt = enonce + assertions d'exemple; pas de system prompt prescrit

## Prompt regime
- **Prompt template**: prouve — pas de template unique impose; les harnesses varient
- **CoT**: variable — certains ajoutent du raisonnement, d'autres generation directe
- **Parsing reponse**: prouve — extraction du code, execution contre assertions
- **Sensibilite prompt mesuree**: a verifier — pas de mesure canonique dans la source primaire

## Scoring
- **Metrique**: pass@k (principalement pass@1 et pass@80 dans le papier original)
- **Budget d'echantillonnage**: prouve — meme logique que HumanEval, gonflable par nombre de samples
- **Post-processing**: prouve — execution des assertions, calcul pass@k

## Version modele
- **Snapshot requis**: non
- **API vs weights**: mixte
- **Reproductibilite declaree**: plausible — subset utilise (full vs sanitized), shots et budget varient selon les evals

## Contamination
- **Surface directe**: prouve — problemes simples publics depuis 2021, largement indexes
- **Surface indirecte**: prouve — les problemes sont de niveau debutant/intermediaire, tres proches d'exercices Python courants dans les corpus de train
- **Mesures anti-contamination**: aucune — benchmark statique public
- **Niveau de risque Mythas**: critique

## Gaming
- **Prompt tuning**: plausible — problemes simples, facilement optimisables par prompt
- **Format fitting**: prouve — problemes basiques et memorisables; un modele peut les resoudre par memorisation plutot que par competence
- **Hill-climbing**: plausible — souvent couple avec HumanEval sur les leaderboards
- **Harness overfitting**: prouve — full vs sanitized, shots, budget, timeout: tout varie et change le score
- **Niveau de risque Mythas**: critique

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: compromis
- **Resume**: Benchmark debutant/intermediaire trop simple et trop public pour mesurer quoi que ce soit de fiable sur les modeles actuels. Contamination quasi-certaine, scores non-comparables entre subsets.
- **Date audit**: 2026-04-19
