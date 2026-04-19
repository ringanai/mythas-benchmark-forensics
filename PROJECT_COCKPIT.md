# MYTHAS - Project Cockpit

## Mission

- exposer le mensonge des benchmarks IA
- cartographier contamination, incomparabilite et benchmark gaming
- construire une logique anti-mensonge plus interpretable
- publier une lecture plus dure que la narrative leaderboard

## Frontiere

- MYTHAS est un projet de forensics benchmark
- MYTHAS n'est pas un projet pour fabriquer une IA tricheuse
- MYTHAS peut etre relie a un ecosysteme plus large, mais garde sa propre verite

## Angle retenu

- pas battre les modeles par BS
- mais:
  - comprendre comment les benchmarks sont manipules
  - montrer pourquoi certains scores publics sont fragiles
  - construire des artefacts critiques plus solides

## Livrables poses

- [x] benchmark map initiale
- [x] schema de fiche d'audit benchmark v0
- [x] famille connaissance auditee: MMLU / MMLU-Pro / MMLU-CF / HELM MMLU
- [x] famille maths auditee: GSM8K / MATH
- [x] famille code auditee: HumanEval / MBPP / SWE-bench
- [x] famille dynamique auditee: LiveBench / LiveCodeBench / BigCodeBench
- [x] famille leaderboard / preference auditee: Chatbot Arena / Open LLM Leaderboard archive
- [x] taxonomie du benchmark gaming
- [x] spec anti-lie bench v0
- [x] template exportable v0
- [x] schema machine-lisible v0
- [x] validateur executable v0
- [x] seuils de verdict v0.5
- [x] README publicisable

## Etat public actuel

- le projet peut deja servir de repo critique public
- les verdicts benchmark sont exprimes en markdown et en JSON pour une partie du corpus
- plusieurs garde-fous machine sont deja poses via schema + fixtures negatives

## Prochaine action unique

- ouvrir la famille `math_verifiable` dans le corpus JSON public avec `GSM8K`, puis continuer la convergence markdown -> JSON

## Questions ouvertes

- quelle voix publique exacte pour Mythas
- jusqu'ou pousser la publication des fiches JSON avant une v1
- faut-il ajouter un mini rapport synthese "claims marketing vs verdict Mythas"

## Risque principal

- glisser de forensics benchmark vers recette de score inflation
- surjouer le lore au lieu de publier des artefacts testables
