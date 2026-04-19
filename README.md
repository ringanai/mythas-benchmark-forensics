# MYTHAS

MYTHAS est un projet de benchmark forensics pour l'IA.

Le but n'est pas de fabriquer un modele "top 1" en trichant.
Le but est de montrer comment des scores impressionnants peuvent raconter
une histoire fausse sur la capacite reelle d'un modele.

En bref:

> MYTHAS mesure la distance entre le score affiche et la verite du modele.

## Ce que le projet defend

- audit des benchmarks publics
- cartographie des surfaces de contamination
- analyse du benchmark gaming
- mise en evidence des ecarts entre claims marketing et capacite reelle
- construction d'une logique anti-mensonge plus dure a gamer

## Ce que le projet refuse

- train on test
- score inflation artificielle
- prompt tuning cible pour un benchmark public
- fuites privees
- acces non autorise
- storytelling de type SOTA sans protocole propre

## Idee centrale

Un benchmark public peut etre:

- contamine
- sature
- non comparable entre papers et leaderboards
- facile a sur-optimiser
- tres eloigne d'un usage reel

Donc:

- un bon score n'implique pas un bon modele
- un meilleur score n'implique pas une meilleure intelligence
- un benchmark peut etre utile tout en restant peu fiable comme ancre

## Ce que contient ce repo

- des fiches d'audit benchmark
- une taxonomie du benchmark gaming
- une spec anti-lie bench
- un schema machine-lisible pour exprimer les fiches
- un validateur local pour verifier la coherence du corpus

## Corpus actuel

Familles deja auditees:

- connaissance / QCM: `MMLU`, `MMLU-Pro`, `MMLU-CF`, `HELM MMLU`
- maths: `GSM8K`, `MATH`
- code: `HumanEval`, `MBPP`, `SWE-bench`
- dynamique: `LiveBench`, `LiveCodeBench`, `BigCodeBench`
- leaderboards / preference: `Chatbot Arena`, `Open LLM Leaderboard archive`

## Lecture recommande

1. `ANTI_LIE_BENCH_V0.md`
2. `BENCHMARK_GAMING_TAXONOMY.md`
3. `V0_VERDICT_THRESHOLDS.md`
4. `V0_FICHE_SCHEMA.json`
5. `validate_v0_fiche.py`
6. `fiches/`

## Etat du chantier

Le projet est deja solide comme observatoire critique.
Il n'est pas encore une suite publique finale.

Aujourd'hui, MYTHAS sait deja:

- re-auditer des benchmarks celebres
- reclasser des benchs sur-vendus
- exprimer ces verdicts dans un format machine-lisible
- bloquer certaines incoherences par validation locale

## Position publique

MYTHAS ne publie pas de recette pour fabriquer la meilleure IA menteuse.
MYTHAS publie:

- pourquoi certains scores ne veulent pas dire ce qu'on croit
- quels protocoles rendent une evaluation interpretable
- quels signaux indiquent qu'un benchmark est trop fragile pour servir d'ancre

## Motto

Le score monte.
La verite, pas forcement.
