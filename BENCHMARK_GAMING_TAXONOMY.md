# MYTHAS - Benchmark Gaming Taxonomy

## But

Transformer les audits benchmark en une taxonomie reusable.
Mythas ne veut pas seulement dire "ce score ment".
Mythas veut dire *comment* il peut mentir, *pourquoi*, et *quels champs minimaux* il faut enregistrer pour le qualifier.

Regle:
- chaque categorie est un mode de distortion
- une meme evaluation peut cumuler plusieurs categories
- une categorie peut etre `prouvee`, `plausible` ou `a verifier` selon la famille auditee

---

## 1. Contamination directe

- **Definition**: des items de test ou leurs variantes tres proches sont deja presents dans les corpus de train ou de synthese du modele.
- **Signal typique**: benchmark public ancien, test telechargeable, mirrors multiples, memorisation d'items.
- **Familles ou c'est deja prouve**:
  - MMLU
  - HumanEval
  - MBPP
  - GSM8K
  - MATH
- **Familles ou c'est reduit mais pas annule**:
  - LiveBench
  - LiveCodeBench
- **Contre-mesure type**: test ferme, separation temporelle forte, decontamination explicite.
- **Champ Mythas a enregistrer**:
  - test public / ferme / mixte
  - date de publication du test
  - mirrors connus
  - surface publique exacte

## 2. Contamination indirecte

- **Definition**: le test lui-meme n'est pas forcement memorise, mais ses solutions, editorials, blogs, repos tiers, walkthroughs ou patches de reference circulent publiquement.
- **Signal typique**: benchmark tres commente, solutions detaillees, repos GitHub publics, samples ouverts.
- **Familles ou c'est deja prouve**:
  - MATH
  - SWE-bench
  - BigCodeBench
  - LiveBench
  - LiveCodeBench
- **Point cle**: une contamination indirecte forte suffit souvent a rendre un score tres facile a sur-interpreter.
- **Champ Mythas a enregistrer**:
  - existence de solutions publiques
  - existence de samples generes publics
  - repos / issues / PRs publics lies a la tache

## 3. Prompt tuning

- **Definition**: le score depend materialement d'un template, d'un system prompt, d'un ordering des choices, d'un shot count ou d'un wrapper specialise.
- **Signal typique**: prompt styles testes, prompt families par modele, scores qui changent fortement avec peu de variations de forme.
- **Familles ou c'est deja prouve**:
  - MMLU-Pro
  - LiveCodeBench
  - BigCodeBench
- **Familles ou c'est fortement plausible**:
  - MMLU
  - LiveBench
  - HumanEval
- **Champ Mythas a enregistrer**:
  - template exact
  - shots
  - CoT autorise / interdit / variable
  - parsing final attendu

## 4. Format fitting

- **Definition**: le modele apprend surtout a satisfaire le format attendu plutot qu'a resoudre la tache de fond.
- **Signal typique**: regex finale, lettre unique, `####`, diff patch attendu, style de reponse prefere, JSON strict.
- **Familles ou c'est deja prouve**:
  - GSM8K
  - HumanEval
  - BigCodeBench
  - Chatbot Arena
- **Familles ou c'est plausible**:
  - MMLU
  - LiveBench
  - LiveCodeBench
- **Champ Mythas a enregistrer**:
  - format de sortie canonique
  - methode de parsing
  - tolerance aux reformulations
  - post-processing applique

## 5. Hill-climbing leaderboard

- **Definition**: optimisation iterative contre un leaderboard public, ses releases, ses subsets ou ses retours communautaires.
- **Signal typique**: updates frequentes, leaderboard centrale, releases publiques, submit loops, score-chasing visible.
- **Familles ou c'est deja prouve**:
  - Chatbot Arena
  - Open LLM Leaderboard archive
  - BigCodeBench
  - LiveBench
  - LiveCodeBench
- **Point cle**: meme un bon benchmark peut devenir une mauvaise cible si tout l'ecosysteme optimise dessus.
- **Champ Mythas a enregistrer**:
  - presence d'un leaderboard public
  - cadence de release
  - feedback loop visible
  - disponibilite des resultats detailles

## 6. Harness overfitting

- **Definition**: adaptation au code d'eval, au checker, au subset, au timeout, au backend ou au scaffolding, plutot qu'a la competence reelle.
- **Signal typique**: le score bouge avec le framework plus qu'avec le modele.
- **Familles ou c'est deja prouve**:
  - SWE-bench
  - HumanEval
  - MBPP
  - LiveCodeBench
  - BigCodeBench
  - Open LLM Leaderboard archive
- **Point cle**: un benchmark peut etre "reproductible" et quand meme fortement harness-sensitive.
- **Champ Mythas a enregistrer**:
  - version du harness
  - checker exact
  - timeout
  - batch size / backend
  - retry / selection / best-of-n

## 7. Style gaming / judge gaming

- **Definition**: optimiser ce qui plait a l'evaluateur humain ou au judge plutot que la competence de fond.
- **Signal typique**: verbosite, politesse, ton, confiance apparente, effet "presentation wins".
- **Familles ou c'est deja prouve**:
  - Chatbot Arena
- **Familles ou c'est plausible**:
  - tout benchmark avec judge humain ou LLM-as-judge
- **Point cle**: ce mode de gaming mesure souvent quelque chose de reel, mais pas necessairement ce que la narration marketing pretend.
- **Champ Mythas a enregistrer**:
  - type de juge
  - anonymisation ou non
  - tie handling
  - distribution des prompts / votants

## 8. Protocol fragmentation

- **Definition**: le meme nom de benchmark recouvre en pratique plusieurs implementations, prompts, subsets ou normalisations non equivalentes.
- **Signal typique**: deux scores "MMLU" ou "leaderboard score" non comparables entre eux.
- **Familles ou c'est deja prouve**:
  - HELM MMLU / MMLU / Open LLM Leaderboard
  - Chatbot Arena
  - LiveBench
  - LiveCodeBench
- **Point cle**: c'est l'une des sources majeures de mensonge benchmark sans qu'il y ait forcement fraude intentionnelle.
- **Champ Mythas a enregistrer**:
  - benchmark exact
  - implementation exacte
  - release / subset
  - prompt regime
  - modele + revision / snapshot

---

## Ce qui est deja bien prouve dans Mythas

- contamination directe
- contamination indirecte
- prompt tuning
- format fitting
- hill-climbing leaderboard
- harness overfitting
- style gaming / judge gaming
- protocol fragmentation

Conclusion locale:
- Mythas a deja assez de preuves pour dire que le mensonge benchmark n'est pas un seul probleme.
- C'est un empilement de modes de distortion qui peuvent se cumuler.

## Ce qui reste a verifier

- seuils pratiques de passage de `fragile` a `compromis`
- poids relatif de chaque categorie dans un verdict final
- maniere de noter les benchmarks hybrides (par ex. benchmark dynamique + leaderboard + judge humain)
- maniere de traiter les APIs proprietaires qui changent silencieusement

## Ce que Mythas doit absolument enregistrer pour qualifier un score

- nom exact du benchmark
- implementation exacte
- release / subset / split
- prompt template ou son absence
- shots / CoT / parsing
- metrique exacte
- budget d'echantillonnage
- post-processing
- version du modele ou snapshot API
- statut public / ferme du test
- nature du juge (exact, humain, LLM, mixte)

## Regle d'interpretation

Un score devient Mythas-compatible seulement si:

1. son protocole est reconstructible
2. ses surfaces de contamination sont nommees
3. ses surfaces de gaming sont nommees
4. sa comparabilite avec d'autres scores est explicitement bornee

Sinon:
- le score peut rester utile
- mais il ne doit pas etre traite comme une verite portable
