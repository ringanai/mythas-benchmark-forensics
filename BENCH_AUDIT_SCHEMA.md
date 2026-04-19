# MYTHAS - Schema de fiche d'audit benchmark

Chaque benchmark audite par Mythas doit avoir une fiche avec ces champs.
Un champ vide = pas encore verifie (pas "non applicable").

---

## Champs obligatoires

### Identite
- **Nom**: nom exact du benchmark
- **Famille**: knowledge / math / code / reasoning / agents / dynamic / arena
- **Source primaire**: URL paper + URL repo/dataset
- **Date de creation**: date de premiere publication

### Acces au test
- **Test public**: oui / non / mixte
- **Detail acces**: quoi est public, quoi est ferme, quoi est sur demande
- **Mirrors connus**: HuggingFace, GitHub forks, blogs avec solutions

### Setup exact
- **Format**: MCQ / open-ended / code generation / repo-level / preference
- **Nombre d'items**: taille du test set
- **Shots**: 0-shot / few-shot / variable
- **Instructions**: system prompt prescrit ou libre

### Prompt regime
- **Prompt template**: template officiel vs libre
- **CoT**: autorise / interdit / variable
- **Parsing reponse**: regex / exact match / model-as-judge / custom
- **Sensibilite prompt mesuree**: oui/non + reference si oui

### Scoring
- **Metrique**: accuracy / pass@k / elo / win-rate / custom
- **Budget d'echantillonnage**: nombre de tentatives, temperature, selection
- **Post-processing**: filtrage, best-of-n, majority vote

### Version modele
- **Snapshot requis**: oui/non — le score est-il lie a une version precise
- **API vs weights**: API datee / weights publics / non specifie
- **Reproductibilite declaree**: le papier donne-t-il assez pour reproduire

### Contamination
- **Surface directe**: items de test dans les corpus de train (prouve/plausible/inconnu)
- **Surface indirecte**: solutions, walkthroughs, blogs, repos tiers
- **Mesures anti-contamination**: separation temporelle, test ferme, decontamination explicite
- **Niveau de risque Mythas**: faible / moyen / eleve / critique

### Gaming
- **Prompt tuning**: adaptation de prompt au format du bench
- **Format fitting**: memorisation de templates de reponse
- **Hill-climbing**: optimisation iterative sur leaderboard
- **Harness overfitting**: adaptation au harness d'eval plutot qu'a la tache
- **Niveau de risque Mythas**: faible / moyen / eleve / critique

### Verdict Mythas
- **Statut audit**: a auditer / en cours / audite / rejete
- **Verdict**: fiable / fragile / compromis / inutilisable
- **Resume**: 1-2 phrases max
- **Date audit**: date de la fiche

---

## Regles
- Chaque valeur est marquee: prouve / plausible / a verifier
- Pas de jugement sans source
- Pas de "tout est compromis" sans preuve specifique
- Le verdict peut changer si de nouvelles preuves arrivent
- Une fiche = un benchmark, pas une famille
