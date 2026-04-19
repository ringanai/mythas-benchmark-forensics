# MYTHAS - Fiche audit: MMLU-CF

## Identite
- **Nom**: MMLU-CF (Contamination-Free)
- **Famille**: knowledge
- **Source primaire**: https://arxiv.org/abs/2412.15194 + https://github.com/microsoft/MMLU-CF
- **Date de creation**: 2024-12

## Acces au test
- **Test public**: mixte — prouve
- **Detail acces**: prouve — validation publique, test ferme; separation explicite pour limiter la contamination
- **Mirrors connus**: prouve — HuggingFace microsoft/MMLU-CF (partie validation)

## Setup exact
- **Format**: MCQ
- **Nombre d'items**: a verifier — taille exacte du test ferme non documentee dans nos sources
- **Shots**: a verifier
- **Instructions**: a verifier

## Prompt regime
- **Prompt template**: a verifier
- **CoT**: a verifier
- **Parsing reponse**: a verifier
- **Sensibilite prompt mesuree**: a verifier

## Scoring
- **Metrique**: accuracy
- **Budget d'echantillonnage**: a verifier
- **Post-processing**: a verifier

## Version modele
- **Snapshot requis**: a verifier
- **API vs weights**: a verifier
- **Reproductibilite declaree**: plausible — la partie test est fermee donc la reproductibilite depend des auteurs

## Contamination
- **Surface directe**: prouve — le test ferme reduit la surface directe; c'est la raison d'etre du benchmark
- **Surface indirecte**: plausible — la validation publique peut devenir cible de hill-climbing
- **Mesures anti-contamination**: prouve — decontamination explicite, separation val/test, distributions proches
- **Niveau de risque Mythas**: faible

## Gaming
- **Prompt tuning**: plausible — val publique peut servir de proxy pour adapter les prompts
- **Format fitting**: a verifier
- **Hill-climbing**: plausible — si le leaderboard utilise la val publique, le risque existe
- **Harness overfitting**: a verifier
- **Niveau de risque Mythas**: moyen

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: fiable
- **Resume**: Variante la plus solide de la famille MMLU. Le test ferme et la decontamination explicite en font une reference methodologique pour Mythas. Points a verifier: taille exacte du test et details de prompt/parsing.
- **Date audit**: 2026-04-19
