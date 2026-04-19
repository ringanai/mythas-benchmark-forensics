# MYTHAS - Fiche audit: MATH

## Identite
- **Nom**: MATH
- **Famille**: math
- **Source primaire**: https://arxiv.org/abs/2103.03874 + https://github.com/hendrycks/math
- **Date de creation**: 2021-03

## Acces au test
- **Test public**: oui - prouve
- **Detail acces**: prouve - repo public avec loaders, code d'eval et lien de telechargement dataset
- **Mirrors connus**: prouve - Hugging Face, forks GitHub, subsets type MATH-500, blogs et jeux de traces avec solutions

## Setup exact
- **Format**: open-ended competition mathematics
- **Nombre d'items**: prouve - 12,500 problemes au total; a verifier - repartition exacte train/test a partir des seules sources primaires lues ici
- **Shots**: variable - 0-shot, few-shot, CoT et self-consistency sont tous utilises dans la litterature ulterieure
- **Instructions**: libre - pas de system prompt unique impose

## Prompt regime
- **Prompt template**: prouve - pas de template canonique unique; les harnesses varient
- **CoT**: plausible - tres fortement favorise par la presence de solutions detaillees pas-a-pas
- **Parsing reponse**: variable - exact match, extraction de reponse finale, normalisation LaTeX ou boxed answer selon les setups
- **Sensibilite prompt mesuree**: a verifier - les sources primaires etablissent surtout la difficulte du benchmark, pas une mesure standardisee de prompt sensitivity

## Scoring
- **Metrique**: accuracy sur la reponse finale
- **Budget d'echantillonnage**: variable - de nombreuses evals ulterieures utilisent self-consistency, best-of-n ou maj vote
- **Post-processing**: plausible - normalisation d'expressions mathematiques et extraction de la reponse finale jouent un role important

## Version modele
- **Snapshot requis**: non - souvent absent ou incomplet dans les comparaisons publiques
- **API vs weights**: mixte
- **Reproductibilite declaree**: plausible - dataset et code publics, mais protocoles de prompt, parsing et budget rendent la comparaison fragile

## Contamination
- **Surface directe**: plausible - benchmark public ancien avec solutions completes et corpus facilement re-ingestables
- **Surface indirecte**: prouve - solutions detaillees, tutoriaux, fine-tunes math et reprises Hugging Face multiplient la surface de contamination
- **Mesures anti-contamination**: aucune - pas de test ferme ni de separation temporelle dans le benchmark original
- **Niveau de risque Mythas**: critique

## Gaming
- **Prompt tuning**: plausible - benchmark tres sensible aux demonstrations et au style de raisonnement impose
- **Format fitting**: plausible - les solutions detaillees et la convention de reponse finale favorisent l'adaptation au format
- **Hill-climbing**: plausible - benchmark central dans la communication "math reasoning", donc forte incitation a optimiser iterativement
- **Harness overfitting**: plausible - parsing, normalisation et budgets de sampling peuvent changer fortement les scores reportes
- **Niveau de risque Mythas**: eleve

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: compromis
- **Resume**: Benchmark exigeant et utile historiquement, mais trop expose pour servir seul de mesure fiable moderne. Les solutions publiques detaillees et les variations de protocole rendent les scores faciles a raconter et difficiles a comparer proprement.
- **Date audit**: 2026-04-19
