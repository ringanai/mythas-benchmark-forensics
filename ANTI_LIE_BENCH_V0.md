# MYTHAS - Anti-lie bench v0

## But

Mythas n'est pas un nouveau benchmark de performance.
C'est un protocole de qualification d'un score.
Un score "anti-lie bench v0" ne pretend pas etre la verite absolue sur un modele.
Il pretend seulement ceci: ce qui est rapporte est reconstructible, borne, et non trivialement gamable.

La spec v0 est minimale, publiable, et explicite sur ce qu'elle refuse de mesurer.

---

## 1. Principes directeurs

1. **Reconstructibilite avant score**
   - un score sans protocole reconstructible est non Mythas-compatible
   - le protocole doit etre reproductible par un tiers a partir des seuls artefacts publies

2. **Bornes explicites de comparabilite**
   - un score Mythas v0 est toujours compare a lui-meme dans le meme regime
   - toute comparaison inter-modeles doit fixer: benchmark exact, implementation, release, prompt regime, snapshot modele

3. **Separation stricte des signaux**
   - competence, preference et scaffolding ne sont jamais agrégés dans un seul chiffre
   - chaque signal a sa propre sortie et sa propre bordure

4. **Contamination nommee**
   - un score v0 documente explicitement ses surfaces de contamination connues
   - l'absence de preuve de contamination n'est pas une preuve d'absence

5. **Gaming nomme**
   - un score v0 documente explicitement les categories de gaming de la taxonomie Mythas auxquelles il reste expose

6. **Public par defaut, ferme ou il le faut**
   - publier tout ce qui discipline le marketing
   - fermer ce qui rend la contamination directe trivialement possible

---

## 2. Briques qui doivent etre fermees

Ces briques ne peuvent pas etre distribuees publiquement si le score v0 veut rester interpretable:

- **Test set canonique**
  - items exacts de test
  - labels / patches / reponses canoniques
  - distribution ferme de la surface d'evaluation

- **Cles de verification**
  - parsers finaux et regex de scoring dans leur version canonique
  - seeds de selection de subset utilises pour le run officiel

- **Snapshots intermediaires de leaderboard**
  - scores individuels par item (pour empecher reverse-engineering direct du test)

**Regle**: la fermeture est minimale, documentee, datee, et accompagnee d'un mecanisme d'evaluation tiers (submission protocol, validateur externe, ou hold-out controle).

---

## 3. Briques qui doivent rester publiques

Ces briques doivent etre publiques pour que le score v0 ne soit pas un acte de foi:

- **Schema de la tache**
  - format d'entree, format de sortie attendu, nature exacte de la metrique

- **Set de validation public**
  - distribution proche du test mais disjoint
  - permet au public de reproduire et critiquer le protocole sans ouvrir le test

- **Code d'eval canonique**
  - harness, checker, timeouts, backend d'execution

- **Taxonomie de gaming applicable**
  - categories de gaming Mythas auxquelles ce score est expose
  - mesures anti-gaming en place (separation temporelle, test ferme, randomization, etc.)

- **Fiche de score**
  - voir section 5

---

## 4. Protocole minimal pour qu'un score reste interpretable

Un score v0 est publie uniquement s'il satisfait les 6 conditions suivantes.

1. **Benchmark identifie sans ambiguite**
   - nom + version + release + subset + split
   - hash ou identifiant stable du set utilise

2. **Implementation unique et figee**
   - version exacte du harness / eval code
   - parametres non masques: timeout, batch size, retry, selection

3. **Prompt regime figé**
   - template exact ou declaration explicite "no template"
   - shots, CoT, system prompt, ordre des choix
   - sensibilite au prompt mesuree ou declaree non mesuree

4. **Budget et selection documentes**
   - temperature, top-p, seed si applicable
   - nombre de samples, politique de selection (greedy, majority, pass@k, best-of-n)
   - budget-equivalent declare pour comparaisons inter-runs

5. **Modele identifie au snapshot**
   - weights publics avec hash, ou API avec date + revision + region si documentee
   - "dernier modele proprietaire" n'est pas un identifiant valide

6. **Surface de contamination et de gaming declarees**
   - pointeur explicite vers les categories Mythas concernees
   - actions prises (test ferme, separation temporelle, randomization, decontamination)

Un score qui manque une de ces 6 conditions n'est pas publie comme score v0.
Il peut rester utile ailleurs, mais il n'est pas Mythas-compatible.

---

## 5. Champs de publication obligatoires

Tout score publie sous le label Mythas v0 doit porter la fiche suivante.
Chaque champ est marque `prouve` / `plausible` / `a verifier`.

- **Identite score**
  - benchmark: nom + version + release + subset + split
  - date du run
  - operateur du run

- **Cible mesuree**
  - signal principal: competence / preference / scaffolding
  - autres signaux explicitement exclus

- **Modele**
  - nom
  - snapshot / revision / hash
  - mode d'acces (weights / API)

- **Harness**
  - version
  - hash du code d'eval
  - backend d'execution
  - timeouts / retries / batch

- **Prompt regime**
  - template
  - shots
  - CoT status
  - system prompt
  - ordre des choix ou randomization

- **Scoring**
  - metrique
  - parser final
  - post-processing
  - budget sampling

- **Contamination declaree**
  - surfaces directes connues
  - surfaces indirectes connues
  - mesures appliquees

- **Gaming declare**
  - categories Mythas applicables
  - mesures appliquees

- **Bornes de comparabilite**
  - avec quels autres scores ce score est comparable
  - avec quels autres scores il n'est pas comparable

- **Statut public / ferme**
  - quoi est publie
  - quoi est ferme
  - mecanisme d'evaluation tiers

---

## 6. Separation des signaux

Mythas v0 refuse l'agregat unique. Trois signaux sont traites separement.

### 6.1 Competence

- mesure: performance sur des taches objectivement scorables
- verifiable par: exact match, execution, preuve formelle
- judge humain interdit pour ce signal
- LLM-as-judge interdit pour ce signal
- exemple de familles: math verifiable, code avec tests de reference fermes

### 6.2 Preference

- mesure: ce qu'un evaluateur humain ou LLM prefere dans une paire
- n'est pas une mesure de competence
- doit documenter: type de juge, anonymisation, tie handling, distribution des prompts, demographie votants si applicable
- ne peut etre publie qu'avec la mention explicite "mesure de preference, pas de competence"

### 6.3 Scaffolding

- mesure: ce que le systeme complet (modele + harness + agent + tools + retry) produit
- doit publier le scaffolding comme citoyen de premiere classe
- un score scaffolding sans description du scaffold n'est pas publiable v0
- comparer scaffolding a competence est interdit dans un meme tableau sans annotation explicite

**Regle de publication**: jamais un seul chiffre agrégé qui melange ces trois signaux.

---

## 7. Arbitrages ouverts

Points que la v0 ne tranche pas encore et qui sont explicitement laisses a une v0.1:

- **Seuils quantitatifs** de passage entre `fiable` / `fragile` / `compromis` / `inutilisable`
- **Poids relatif** des categories de gaming dans un verdict agrégé (si un verdict agrégé est un jour produit)
- **Traitement formel** des benchmarks hybrides (dynamique + leaderboard + judge)
- **Protocole de traitement** des APIs proprietaires a drift silencieux
- **Cadence de re-audit** d'un benchmark dans le temps
- **Gouvernance du test ferme** (qui detient, qui audite, qui peut soumettre)

Ces points sont ouverts mais pas ignores: un score v0 doit au minimum declarer sa position de travail sur chacun.

---

## 8. Ce que Mythas refuse explicitement

Mythas v0 refuse de produire ou d'endosser:

- un score unique agrégé qui melange competence, preference et scaffolding
- un score dont le protocole n'est pas reconstructible a partir des artefacts publies
- un score reportee contre un modele proprietaire sans snapshot / revision identifiable
- une comparaison inter-modeles qui n'explicite pas ses bornes de comparabilite
- une phrase de type "meilleur modele" sans protocole ni bornes
- un benchmark purement public dont la contamination directe est probable mais non mesuree, publie comme verite
- un leaderboard traite comme cour supreme du vrai
- un chiffre de preference humaine publie comme mesure de competence
- un chiffre scaffolding publie comme mesure de competence du modele seul
- tout protocole dont le but est d'ameliorer frauduleusement un score ou de contaminer un jeu de test
- toute technique d'acces non autorise a des tests fermes ou a des donnees privees

---

## 9. Forme du score v0

Un score v0 est publie comme un triplet + une fiche:

- triplet: (signal, valeur, regime)
  - exemple: (competence, pass@1 = 0.312, regime = `LiveCodeBench release_v4 / scenario code_generation_lite / temp 0.0 / single sample / checker default / snapshot 2026-03-12 / harness hash X`)
- fiche: section 5 complete

Une absence de fiche = score non publie.
Une fiche incomplete = score en statut `a verifier`, jamais promu en statut `prouve`.

---

## 10. Prochains chantiers apres v0

- choisir un premier cas d'ecole pour tester la spec de bout en bout (candidat prioritaire: fiche MMLU-CF + une competence code dynamique)
- formaliser un template de fiche v0 exportable (markdown ou JSON)
- definir un protocole minimal de re-audit temporel d'un benchmark
- definir les regles de soumission tierce pour un test ferme
