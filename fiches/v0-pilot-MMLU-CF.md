# MYTHAS - Pilot v0: MMLU-CF

Premier cas d'ecole pour tester la spec `ANTI_LIE_BENCH_V0.md` de bout en bout.
Objectif: voir ce qui tient, ce qui casse, et ce qui sort en `a verifier` quand on applique les 10 champs obligatoires a un benchmark deja audite comme `fiable`.

Ce document ne publie pas un score. Il teste si la spec v0 produit une fiche reconstructible meme sans run reel.

---

## 0. Statut de fiche

- **Type de fiche**: `pilote sans run` — prouve
- **Niveau d'ancrage anti-lie**: `ancrage fort` (potentiel) — plausible
  - justification: MMLU-CF dispose d'un test ferme + decontamination explicite cote design; l'ancrage fort reste conditionne a la documentation d'un mecanisme d'evaluation tiers (section 10), aujourd'hui `a verifier`
- **Justification du statut**: fiche ouverte pour stresser la spec v0 sur un benchmark audite `fiable`; aucun run produit, aucun score publie; reclassable vers `score v0 publie, ancrage fort` si et seulement si la gouvernance du test ferme (submission protocol) est documentee et si les champs harness/prompt/modele sont figes

---

## 1. Identite score

- **Benchmark**: MMLU-CF — prouve
- **Version / release / subset / split**: a verifier — le papier annonce validation publique + test ferme, mais la version exacte utilisable pour un run Mythas-compatible n'est pas fixee dans nos sources
- **Hash / identifiant stable du set**: a verifier
- **Date du run**: non applicable (fiche pilote, pas un run)
- **Operateur du run**: non applicable

## 2. Cible mesuree

- **Signal principal**: competence — prouve (MCQ accuracy, parsable)
- **Signaux explicitement exclus**: preference, scaffolding — prouve

## 3. Modele

- **Nom / snapshot / revision / hash**: non applicable ici
- **Mode d'acces**: non applicable ici
- **Regle Mythas**: "dernier modele proprietaire" interdit comme identifiant — prouve

## 4. Harness

- **Version / hash du code d'eval**: a verifier — le repo `microsoft/MMLU-CF` existe mais la version canonique a figer pour Mythas v0 n'est pas encore choisie
- **Backend d'execution**: a verifier
- **Timeouts / retries / batch**: a verifier

## 5. Prompt regime

- **Template**: a verifier
- **Shots**: a verifier
- **CoT**: a verifier
- **System prompt**: a verifier
- **Ordre des choix / randomization**: a verifier — point critique, MMLU est connu pour etre sensible a l'ordre

## 6. Scoring

- **Metrique**: accuracy — prouve
- **Parser final**: a verifier
- **Post-processing**: a verifier
- **Budget sampling**: a verifier (greedy / majority / best-of-n)

## 7. Contamination declaree

- **Surface directe**: prouve — test ferme, decontamination explicite par les auteurs
- **Surface indirecte**: plausible — la validation publique peut devenir cible de tuning et de hill-climbing
- **Mesures appliquees**: prouve — separation val/test, distributions proches, test non distribue

## 8. Gaming declare (categories Mythas)

- **Contamination directe**: mitigee — prouve
- **Contamination indirecte**: residuelle sur validation publique — plausible
- **Prompt tuning**: expose via validation publique — plausible
- **Format fitting**: residuel (MCQ a 4 choix, patterns classiques) — plausible
- **Hill-climbing leaderboard**: possible si leaderboard lit la val publique — plausible
- **Harness overfitting**: a verifier
- **Style gaming / judge gaming**: non applicable (pas de juge) — prouve
- **Protocol fragmentation**: risque heritee du nom MMLU — plausible

## 9. Bornes de comparabilite

- **Comparable a**: uniquement d'autres scores MMLU-CF produits sous le meme harness, meme prompt regime, meme snapshot modele, meme politique de sampling — prouve
- **Non comparable a**: scores MMLU original, MMLU-Pro, HELM MMLU, ni entre implementations differentes de MMLU-CF — prouve
- **Regle v0**: jamais publier une comparaison inter-modeles sans fixer ces 5 axes — prouve

## 10. Statut public / ferme

- **Publie**: schema de tache, validation publique, code d'eval, papier — prouve
- **Ferme**: items et labels du test, par design — prouve
- **Mecanisme d'evaluation tiers**: a verifier — la gouvernance du test ferme (qui soumet, qui audite, cadence) n'est pas encore decrite dans nos sources; renvoyer a l'arbitrage ouvert v0.1

---

## Lecture pilote

Ce que la spec v0 attrape proprement sur MMLU-CF:
- prouve - separation claire des 3 signaux; MMLU-CF tombe net cote competence
- prouve - bornes de comparabilite sortent comme contrainte non-triviale: meme un benchmark "fiable" n'est pas intercomparable sans fixer 5 axes
- prouve - contamination directe est marquee `mitigee` sans etre declaree `absente`, conformement au principe "absence de preuve n'est pas preuve d'absence"

Ce que la spec v0 laisse en `a verifier` meme sur un benchmark fiable:
- prompt regime complet (template, shots, ordre)
- harness canonique a figer
- parser final et post-processing
- mecanisme de soumission tierce pour le test ferme

Ce que ce pilote enseigne pour la v0.1:
- a verifier - un benchmark peut etre `fiable` au niveau design et rester massivement `a verifier` au niveau fiche v0; la spec doit probablement expliciter ce decalage
- a verifier - sans gouvernance du test ferme documentee, un score MMLU-CF "Mythas v0" reste dependant des auteurs; ajouter ce point comme condition bloquante ou simple clause a divulguer
- a verifier - champs prompt regime et harness sortent systematiquement en `a verifier` tant qu'aucun run reel n'est fait; prevoir un statut fiche "pilote sans run" distinct de "score v0 publie"

## Verdict pilote

- **Spec v0 applicable a MMLU-CF**: oui — prouve
- **Score v0 directement publiable sans run**: non — prouve (manque harness, prompt, snapshot modele)
- **Blocage principal pour un vrai run v0**: mecanisme d'evaluation tiers sur le test ferme — a verifier
- **Date fiche pilote**: 2026-04-19
