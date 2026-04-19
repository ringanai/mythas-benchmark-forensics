# MYTHAS - Pilot v0: LiveCodeBench

Deuxieme cas d'ecole pour tester la spec `ANTI_LIE_BENCH_V0.md` de bout en bout.
Objectif: stresser la spec sur un benchmark code dynamique public, leaderboarde, versionne et multi-scenarios, la ou le pilote MMLU-CF ne pouvait pas exposer les contraintes de release, scaffolding et sampling.

Ce document ne publie pas un score. Il teste si la spec v0 tient face a un benchmark `fragile` au verdict Mythas, avec une surface d'eval beaucoup plus riche en knobs.

---

## 0. Statut de fiche

- **Type de fiche**: `pilote sans run` — prouve
- **Niveau d'ancrage anti-lie**: `borne publique` — prouve
  - justification: LiveCodeBench n'a pas de test ferme par design (section 10 = `aucune fermeture`, mecanisme d'evaluation tiers = `aucun`); la regle de sortie du template interdit le statut `ancrage fort` sans soumission tierce; LiveCodeBench est donc reclassable au mieux en `score v0 publie, public-only` sous reserve de fixer les 8 axes de comparabilite (section 9)
- **Justification du statut**: fiche ouverte pour stresser la spec v0 sur un benchmark audite `fragile`, public, leaderboarde, versionne; aucun run produit, aucun score publie

---

## 1. Identite score

- **Benchmark**: LiveCodeBench — prouve
- **Version / release / subset / split**: a verifier — les releases `release_v1` a `release_v6` existent publiquement, mais aucune version canonique Mythas v0 n'est fixee; un score publie doit nommer la release exacte + le scenario + eventuellement le sous-set `code_generation_lite`
- **Hash / identifiant stable du set**: a verifier — repo et HuggingFace `livecodebench/*` sont publics, mais le hash du snapshot utilise doit etre fige au moment du run
- **Fenetre temporelle**: a verifier — `start_date` / `end_date` sont des parametres natifs; un score sans fenetre declaree est non-Mythas-compatible par design
- **Date du run**: non applicable (fiche pilote, pas un run)
- **Operateur du run**: non applicable

## 2. Cible mesuree

- **Signal principal**: competence — prouve si et seulement si le scenario est strictement objectivement scorable (code generation avec tests caches, code execution, test output prediction)
- **Scaffolding**: a verifier — self-repair peut deriver vers du scaffolding si des retries / feedbacks sont introduits; dans ce cas, reclasser le signal comme scaffolding, pas competence
- **Signaux explicitement exclus**: preference — prouve (aucun juge humain ni LLM-as-judge dans le pipeline canonique)

## 3. Modele

- **Nom / snapshot / revision / hash**: non applicable ici
- **Mode d'acces**: non applicable ici — LiveCodeBench supporte weights locaux (vLLM) et APIs
- **Regle Mythas**: "dernier modele proprietaire" interdit comme identifiant — prouve; un run sur API doit fixer date + revision (+ region si documentee)

## 4. Harness

- **Version / hash du code d'eval**: a verifier — repo public, mais la version canonique a figer pour Mythas v0 n'est pas choisie
- **Checker**: a verifier — un checker derive d'APPS existe et a ete modifie dans le temps; le hash du checker doit etre fige
- **Backend d'execution**: a verifier — impacte temps, flakiness et timeouts
- **Timeouts / retries / batch**: a verifier — ces parametres changent materialement le score
- **Options specifiques**: a verifier — `code_generation_lite`, `continue_existing`, parallelisme d'execution

## 5. Prompt regime

- **Template**: a verifier — templates model-family-specifiques dans le code; ce n'est pas un bug mais un fait a declarer
- **Shots**: a verifier — pas de regime few-shot canonique unique
- **CoT**: variable — prouve qu'un mode CoT explicite existe pour `codeexecution`; son activation doit etre declaree
- **System prompt**: a verifier
- **Ordre des choix / randomization**: non applicable (pas de MCQ)

## 6. Scoring

- **Metrique**: `pass@1` ou `pass@5` selon scenario — prouve
- **Parser final**: prouve — execution automatisee, pas de parsing textuel
- **Post-processing**: a verifier — extraction de code, stripping de markdown, handling d'imports manquants
- **Budget sampling**: a verifier — la doc canonique mentionne `n=10` et `temperature=0.2` pour la generation; un score publie doit fixer `n`, `temperature`, `top-p`, `seed`
- **Politique de selection**: a verifier — greedy vs majority vs pass@k vs best-of-n

## 7. Contamination declaree

- **Surface directe**: plausible — reduite par la separation temporelle sur les problemes post-cutoff, mais pas absente; items de concours migrent vers walkthroughs publics en quelques semaines
- **Surface indirecte**: prouve — editorials, solutions GitHub, forums de competitive programming, releases publiques et leaderboard alimentent une surface secondaire
- **Mesures appliquees**: prouve — collecte continue, versioning par release, filtrage par fenetre de dates, consigne de tester sur du "post-cutoff"
- **Regle Mythas**: la fenetre temporelle utilisee doit etre declaree explicitement; un score sur une fenetre couvrant le cutoff du modele n'est pas Mythas-compatible pour le signal competence

## 8. Gaming declare (categories Mythas)

- **Contamination directe**: mitigee sur problemes recents, residuelle sinon — plausible
- **Contamination indirecte**: structurelle — prouve (editorials + GitHub)
- **Prompt tuning**: expose par design — prouve (templates model-family-specifiques)
- **Format fitting**: plausible — scenarios et attentes de sortie sont publics
- **Hill-climbing leaderboard**: prouve — leaderboard public, releases successives, pression d'optimisation
- **Harness overfitting**: prouve — checker, `code_generation_lite`, timeouts, fenetre temporelle, `continue_existing` changent materialement le score
- **Style gaming / judge gaming**: non applicable (pas de juge) — prouve
- **Protocol fragmentation**: prouve — release + scenario + fenetre + checker + backend forment un espace de protocoles trop grand pour un "score LiveCodeBench" nu

## 9. Bornes de comparabilite

- **Comparable a**: uniquement d'autres scores LiveCodeBench produits sous meme release, meme scenario, meme fenetre temporelle, meme checker, meme harness, meme prompt regime, meme budget, meme snapshot modele — prouve
- **Non comparable a**: HumanEval, MBPP, SWE-bench, BigCodeBench, ni entre releases differentes de LiveCodeBench, ni entre fenetres temporelles differentes — prouve
- **Regle v0**: publier une comparaison inter-modeles sans fixer ces 8 axes est interdit — prouve

## 10. Statut public / ferme

- **Publie**: schema de tache, datasets par release, code d'eval, checker, leaderboard — prouve
- **Ferme**: rien n'est ferme au sens Mythas du terme (pas de test ferme) — prouve
- **Mecanisme d'evaluation tiers**: absent — prouve
- **Consequence**: LiveCodeBench ne remplit pas la condition "briques fermees" de la spec v0 section 2; un score v0 LiveCodeBench est publiable comme mesure de competence bornee, pas comme ancre anti-lie de reference

---

## Lecture pilote

Ce que la spec v0 attrape proprement sur LiveCodeBench:
- prouve - la fenetre temporelle sort comme axe de comparabilite non negociable; un score sans fenetre est rejete par la spec
- prouve - la separation des signaux force a reclasser self-repair comme potentiellement scaffolding, pas competence
- prouve - la taxonomie gaming section 8 nomme explicitement prompt tuning, harness overfitting, hill-climbing et protocol fragmentation comme surfaces actives
- prouve - 8 axes de comparabilite sortent contre 5 sur MMLU-CF; la spec scale bien en richesse de protocole

Ce que la spec v0 laisse exposer comme limite structurelle:
- prouve - LiveCodeBench ne peut pas satisfaire la section 2 (briques fermees) parce qu'il n'a pas de test ferme par design
- prouve - la spec v0 ne refuse pas LiveCodeBench, elle refuse le score LiveCodeBench qui se presenterait comme ancre anti-lie; il reste publiable comme mesure bornee avec statut `public-only`
- a verifier - ajouter en v0.1 un statut fiche explicite `public-only benchmark` distinct de `benchmark a test ferme`, pour que la lecture de la fiche ne soit pas ambigue

Ce que ce pilote enseigne pour la v0.1:
- a verifier - formaliser l'obligation de declarer la fenetre temporelle + la release comme champ de publication dedie, au-dessus du champ release/subset generique
- a verifier - formaliser le reclassement signal competence -> scaffolding quand retry/feedback apparait (self-repair, agents, multi-turn)
- a verifier - prevoir un champ explicite `niveau d'ancrage anti-lie` sur la fiche, avec au moins 2 niveaux: `ancrage fort` (test ferme + soumission tierce) et `borne publique` (pas de test ferme, score borne mais non ancre)
- a verifier - la liste des 8 axes de comparabilite LiveCodeBench suggere que la v0.1 doit publier un gabarit d'axes par famille de benchmark, pas un gabarit unique

## Verdict pilote

- **Spec v0 applicable a LiveCodeBench**: oui — prouve
- **Score v0 directement publiable sans run**: non — prouve (manque release exacte, fenetre, harness, prompt, snapshot modele, budget)
- **Score v0 utilisable comme ancre anti-lie**: non — prouve (pas de test ferme, pas de soumission tierce)
- **Score v0 utilisable comme borne publique de competence**: oui, sous reserve de fixer les 8 axes de comparabilite — plausible
- **Blocage principal pour un vrai run v0**: choix canonique de release + fenetre + checker + harness; secondaire: declaration explicite du signal (competence vs scaffolding) pour self-repair
- **Date fiche pilote**: 2026-04-19
