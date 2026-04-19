# MYTHAS - Fiche audit: LiveCodeBench

## Identite
- **Nom**: LiveCodeBench
- **Famille**: dynamic / code
- **Source primaire**: https://arxiv.org/abs/2403.07974 + https://github.com/LiveCodeBench/LiveCodeBench
- **Date de creation**: 2024-03

## Acces au test
- **Test public**: oui - prouve
- **Detail acces**: prouve - les jeux de donnees, releases, code d'eval, leaderboard et explorer sont publics; le benchmark roule par versions successives `release_v1` a `release_v6`
- **Mirrors connus**: prouve - HuggingFace `livecodebench/*`, website, leaderboard public, espaces d'exploration des generations

## Setup exact
- **Format**: benchmark code multi-scenarios - code generation, self-repair, code execution, test output prediction
- **Nombre d'items**: prouve - 400 problemes dans `release_v1`, 1055 problemes dans `release_v6`; la taille evolue avec les releases
- **Shots**: a verifier - la generation standard part du probleme seul, mais les sources consultees ne fixent pas un regime few-shot canonique unique
- **Instructions**: prouve - prompts et styles de formatage variables selon la famille de modele; le code execution supporte aussi un mode CoT explicite

## Prompt regime
- **Prompt template**: prouve - templates model-family-specifiques dans le code (`generation.py` et styles associes)
- **CoT**: variable - prouve - un mode CoT explicite existe pour `codeexecution`, alors que d'autres scenarios restent en generation plus directe
- **Parsing reponse**: prouve - execution/checking automatise, avec un checker derive d'APPS et des evaluateurs specifiques aux scenarios
- **Sensibilite prompt mesuree**: a verifier - pas de mesure canonique unique de prompt sensitivity dans les sources primaires consultees

## Scoring
- **Metrique**: mixte - prouve - `pass@1` et `pass@5` pour la code generation; autres scores scenario-specifiques selon execution / prediction / repair
- **Budget d'echantillonnage**: prouve - la config standard documentee pour la generation utilise `n=10` et `temperature=0.2`; timeout et parallelisme peuvent faire varier les resultats
- **Post-processing**: prouve - checker modifie, option `code_generation_lite` par defaut, fenetres temporelles `start_date` / `end_date`, reprises d'evals avec `continue_existing`

## Version modele
- **Snapshot requis**: prouve - le benchmark est explicitement lie a des fenetres temporelles de problemes et a des releases versionnees; la date d'evaluation compte
- **API vs weights**: mixte - prouve - open models via vLLM/local path et closed models via API sont tous les deux supportes
- **Reproductibilite declaree**: plausible - code et data sont publics, mais les releases mouvantes, checker updates, timeouts et derive des APIs rendent la reproduction exacte delicate

## Contamination
- **Surface directe**: plausible - nettement reduite par rapport a HumanEval sur les problemes les plus recents, mais les sujets de concours, editorials et solutions deviennent vite publics
- **Surface indirecte**: prouve - solutions de concours, GitHub, errata, releases publiques et leaderboard exposent rapidement une surface secondaire
- **Mesures anti-contamination**: prouve - collecte continue dans le temps, versioning des releases, filtrage par fenetre de dates pour tester des modeles sur du "nouveau"
- **Niveau de risque Mythas**: moyen

## Gaming
- **Prompt tuning**: prouve - prompts et styles dependent explicitement de la famille de modele
- **Format fitting**: plausible - les scenarios et leurs attentes de sortie sont suffisamment publics pour inviter un fitting benchmark-specifique
- **Hill-climbing**: prouve - leaderboard publique et releases successives encouragent une optimisation iterative
- **Harness overfitting**: prouve - checker modifie, `code_generation_lite`, timeouts et choix de fenetre temporelle affectent fortement le score
- **Niveau de risque Mythas**: eleve

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: fragile
- **Resume**: LiveCodeBench corrige une grande partie du mensonge HumanEval/MBPP grace a la separation temporelle et au scope multi-scenarios. Mais sa nature publique, versionnee et riche en knobs d'evaluation garde une forte surface de tuning et de non-comparabilite.
- **Date audit**: 2026-04-19
