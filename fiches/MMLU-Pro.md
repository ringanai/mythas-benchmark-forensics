# MYTHAS - Fiche audit: MMLU-Pro

## Identite
- **Nom**: MMLU-Pro
- **Famille**: knowledge
- **Source primaire**: https://arxiv.org/abs/2406.01574 + https://github.com/TIGER-AI-Lab/MMLU-Pro
- **Date de creation**: 2024-06

## Acces au test
- **Test public**: oui — prouve
- **Detail acces**: prouve — dataset, scripts d'eval et prompts publics sur GitHub et HuggingFace
- **Mirrors connus**: prouve — HuggingFace TIGER-Lab/MMLU-Pro, GitHub forks

## Setup exact
- **Format**: MCQ 10 choix (A-J)
- **Nombre d'items**: prouve — 12032 items
- **Shots**: variable — 5-shot CoT recommande par les auteurs
- **Instructions**: prouve — 24 prompt styles testes dans le papier

## Prompt regime
- **Prompt template**: prouve — les auteurs fournissent des templates mais les implementeurs varient
- **CoT**: prouve — CoT recommande; sans CoT la performance chute significativement
- **Parsing reponse**: variable — extraction de lettre apres raisonnement
- **Sensibilite prompt mesuree**: prouve — ~2% de variation (24 styles), contre ~4-5% sur MMLU original

## Scoring
- **Metrique**: accuracy
- **Budget d'echantillonnage**: generalement 1 tentative (greedy)
- **Post-processing**: extraction de la lettre finale apres CoT

## Version modele
- **Snapshot requis**: non specifie
- **API vs weights**: mixte
- **Reproductibilite declaree**: plausible — scripts publics mais prompt/parsing variables

## Contamination
- **Surface directe**: plausible — dataset public depuis juin 2024
- **Surface indirecte**: plausible — scripts et setup publics facilitent l'adaptation
- **Mesures anti-contamination**: prouve — espace de reponse elargi (10 choix) reduit le guess rate mais pas la contamination
- **Niveau de risque Mythas**: eleve

## Gaming
- **Prompt tuning**: plausible — bien que moins sensible que MMLU, le format reste optimisable
- **Format fitting**: plausible — 10 choix reduit le hasard mais le pattern reste reconnaissable
- **Hill-climbing**: plausible — deja present sur plusieurs leaderboards
- **Harness overfitting**: plausible — differences CoT/non-CoT peuvent etre exploitees
- **Niveau de risque Mythas**: moyen

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: fragile
- **Resume**: Amelioration reelle sur MMLU (moins prompt-sensible, plus discriminant) mais reste public et optimisable. Meilleur que MMLU, insuffisant seul.
- **Date audit**: 2026-04-19
