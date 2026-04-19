# MYTHAS - Fiche audit: Chatbot Arena

## Identite
- **Nom**: Chatbot Arena
- **Famille**: arena / leaderboard
- **Source primaire**: https://arxiv.org/abs/2403.04132 + https://www.lmsys.org/blog/2024-03-01-policy/
- **Date de creation**: 2023-05

## Acces au test
- **Test public**: mixte - prouve
- **Detail acces**: prouve - la plateforme est publique et open source, mais il n'existe pas de test set fixe totalement ouvert; seules des tranches periodiques des votes sont publiees, et certains modeles restent anonymises hors leaderboard
- **Mirrors connus**: prouve - `lmarena.ai`, blog / policy LMSYS, FastChat sur GitHub, jeux de preference publics mentionnes dans la policy

## Setup exact
- **Format**: preference humaine pairwise sur conversations ouvertes
- **Nombre d'items**: prouve - pas de test set fixe; flux continu de prompts utilisateurs et de batailles
- **Shots**: variable - prouve - depend entierement du prompt de l'utilisateur
- **Instructions**: prouve - pas de system prompt d'evaluation canonique unique cote utilisateur; la tache est ouverte

## Prompt regime
- **Prompt template**: prouve - aucun template unique; les prompts viennent de la foule
- **CoT**: variable - plausible - selon les modeles et les interfaces, mais pas impose par le benchmark
- **Parsing reponse**: prouve - vote humain pairwise avec tie possible; le signal est ensuite agrege en rating
- **Sensibilite prompt mesuree**: non - prouve - il n'y a pas de prompt canonique a perturber; la variance vient plutot de la distribution des prompts et des votants

## Scoring
- **Metrique**: prouve - rating de type arena derive des comparaisons pairwise; la plateforme est passee de l'Elo online a Bradley-Terry / MLE avec intervalles de confiance
- **Budget d'echantillonnage**: prouve - le score depend directement du volume de votes, des matchups observes et de la couverture des confrontations
- **Post-processing**: prouve - bootstrap / intervalles de confiance, ties comptees comme demi-victoires, publication periodique partielle des donnees

## Version modele
- **Snapshot requis**: prouve - les auteurs distinguent explicitement des versions d'API comme `gpt-4-0314` vs `gpt-4-0613` car la performance peut changer
- **API vs weights**: mixte - prouve - modeles open-weight et APIs proprietaires coexistent dans la meme arena
- **Reproductibilite declaree**: fragile - plausible - le code est ouvert, mais la distribution reelle des prompts, des votes et des matchups n'est pas pleinement rejouable publiquement

## Contamination
- **Surface directe**: faible - plausible - pas de test set statique unique a memoriser comme sur MMLU ou HumanEval
- **Surface indirecte**: prouve - publication periodique de votes, reveals de classements, blog updates et data sharing partiel aux providers creent une surface secondaire pour optimiser le comportement
- **Mesures anti-contamination**: prouve - publication de seulement 20% des votes pour mitiger overfitting / leakage; anonymisation partielle des modeles hors leaderboard
- **Niveau de risque Mythas**: moyen

## Gaming
- **Prompt tuning**: prouve - les modeles peuvent etre post-traines pour plaire a la distribution de prompts/votants de l'arena
- **Format fitting**: prouve - style, longueur, politesse, surete apparente et verbosite peuvent influencer les preferences sans refléter la competence brute
- **Hill-climbing**: prouve - leaderboard publique, sorties mediatiques et previews de nouveaux modeles poussent a l'optimisation arena-specifique
- **Harness overfitting**: plausible - moins un harness technique qu'un overfitting au mix prompts/votes/rules de l'arena
- **Niveau de risque Mythas**: critique

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: fragile
- **Resume**: Chatbot Arena capture un signal humain vivant qu'aucun benchmark statique ne voit, mais il reste une mesure de preference situee, fortement sensible au style, au sampling des votes et aux versions d'API. Tres utile pour observer ce que les gens preferent; dangereux si on le lit comme une verite generale sur "le meilleur modele".
- **Date audit**: 2026-04-19
