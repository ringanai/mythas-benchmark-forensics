# MYTHAS - Fiche audit: LiveBench

## Identite
- **Nom**: LiveBench
- **Famille**: dynamic
- **Source primaire**: https://arxiv.org/abs/2406.19314 + https://github.com/LiveBench/LiveBench
- **Date de creation**: 2024-06

## Acces au test
- **Test public**: mixte - prouve
- **Detail acces**: prouve - releases, code, questions, model answers et judgments sont publies; cependant la release la plus recente n'est pas toujours entierement publique, et le repo recommande parfois d'utiliser la derniere release pleinement publiee
- **Mirrors connus**: prouve - HuggingFace `livebench/*`, `livebench/model_answer`, `livebench/model_judgment`, leaderboard `livebench.ai`, changelog GitHub

## Setup exact
- **Format**: multi-categorie open-ended a ground-truth objectif (math, reasoning, coding, language, data analysis, instruction following)
- **Nombre d'items**: prouve - 960 questions dans la suite initiale; le total evolue ensuite avec les releases mensuelles
- **Shots**: a verifier - les sources primaires ne fixent pas un regime few-shot canonique unique pour toutes les taches
- **Instructions**: prouve - les consignes sont embarquees dans les fichiers de questions et varient selon la tache; pas de system prompt global unique documente

## Prompt regime
- **Prompt template**: prouve - variable par tache; le repo documente meme comment remplacer les `question.jsonl` pour tester d'autres prompts
- **CoT**: variable - plausible - certaines questions imposent un format de reponse explicite ou un raisonnement intermediaire, mais il n'y a pas de regle canonique unique
- **Parsing reponse**: prouve - scoring objectif et ground-truth par tache, sans LLM judge comme mecanisme canonique
- **Sensibilite prompt mesuree**: a verifier - pas de mesure unique de prompt sensitivity trouvee dans les sources primaires consultees

## Scoring
- **Metrique**: prouve - scores objectifs par tache/categorie agreges au leaderboard
- **Budget d'echantillonnage**: plausible - temperature, max tokens, provider et options d'execution sont configurables; les scores sont donc sensibles aux parametres s'ils ne sont pas declares
- **Post-processing**: prouve - retries sur erreurs API, jugements ground-truth specifiques a chaque tache, erreurs persistantes comptees comme reponses incorrectes

## Version modele
- **Snapshot requis**: plausible - benchmark mensuel + derive API => la date exacte d'evaluation et l'identite du modele comptent reellement
- **API vs weights**: mixte - prouve - les APIs sont le chemin recommande; l'inference locale est explicitement deconseillee / peu maintenue
- **Reproductibilite declaree**: plausible - code, questions, answers et judgments sont publies, mais la derive des APIs et le decalage entre release courante et release publique complete limitent la reproductibilite stricte

## Contamination
- **Surface directe**: plausible - plus faible sur les releases toutes recentes fondees sur des sources recentes, mais non nulle des qu'une release devient publique
- **Surface indirecte**: prouve - questions, answers, judgments, changelog et scripts d'eval publics constituent une surface secondaire croissante de tuning
- **Mesures anti-contamination**: prouve - releases mensuelles, questions basees sur des sources recentes, scoring objectif, refus du LLM judge comme socle principal
- **Niveau de risque Mythas**: moyen

## Gaming
- **Prompt tuning**: plausible - les categories et les formats de reponse publics permettent un tuning release-specifique ou tache-specifique
- **Format fitting**: plausible - les scorers objectifs et les formats attendus peuvent etre cibles a mesure que les releases s'accumulent
- **Hill-climbing**: prouve - leaderboard public + releases regulieres = incitation directe a optimiser itativement
- **Harness overfitting**: plausible - les scripts de scoring, le choix de release et les dependances des taches coding peuvent devenir la vraie cible
- **Niveau de risque Mythas**: moyen

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: fragile
- **Resume**: LiveBench est l'un des meilleurs designs publics pour reduire la contamination directe, mais il ne sort pas du cycle public release -> optimisation -> nouvelle release. Tres utile comme modele methodologique, pas comme ancre finale de verite.
- **Date audit**: 2026-04-19
