# MYTHAS - Fiche audit: HELM MMLU

## Identite
- **Nom**: HELM MMLU
- **Famille**: knowledge / methodo
- **Source primaire**: https://crfm.stanford.edu/2024/05/01/helm-mmlu.html
- **Date de creation**: 2024-05

## Acces au test
- **Test public**: oui — prouve (utilise le meme test set que MMLU)
- **Detail acces**: prouve — HELM standardise le protocole mais les items sont ceux de MMLU original
- **Mirrors connus**: identiques a MMLU

## Setup exact
- **Format**: MCQ 4 choix (meme que MMLU)
- **Nombre d'items**: prouve — 57 sujets (MMLU complet) vs 5 sujets (HELM Lite)
- **Shots**: prouve — standardise par HELM mais differe de HELM Lite
- **Instructions**: prouve — HELM impose un protocole mais les scores hors-HELM ne suivent pas le meme

## Prompt regime
- **Prompt template**: prouve — HELM fixe son propre template
- **CoT**: a verifier
- **Parsing reponse**: prouve — standardise dans HELM
- **Sensibilite prompt mesuree**: prouve — HELM documente que les scores varient selon le protocole utilise

## Scoring
- **Metrique**: accuracy
- **Budget d'echantillonnage**: standardise dans HELM
- **Post-processing**: standardise dans HELM

## Version modele
- **Snapshot requis**: prouve — HELM date ses evaluations
- **API vs weights**: mixte
- **Reproductibilite declaree**: prouve — c'est l'objectif central de HELM: rendre les comparaisons reproductibles

## Contamination
- **Surface directe**: identique a MMLU — critique
- **Surface indirecte**: identique a MMLU — critique
- **Mesures anti-contamination**: aucune au niveau des items (meme test set)
- **Niveau de risque Mythas**: critique (herite de MMLU)

## Gaming
- **Prompt tuning**: prouve — HELM montre que les scores varient selon le protocole; les scores marketing hors-HELM sont potentiellement optimises
- **Format fitting**: identique a MMLU
- **Hill-climbing**: plausible — la standardisation HELM reduit mais n'elimine pas
- **Harness overfitting**: prouve — le point central de HELM est que les harnesses different et produisent des scores differents
- **Niveau de risque Mythas**: eleve

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: fragile
- **Resume**: Pas un benchmark separe mais une couche de standardisation sur MMLU. Valeur principale: prouver que "score MMLU" sans protocole est ambigu. Herite des faiblesses de contamination de MMLU.
- **Date audit**: 2026-04-19
