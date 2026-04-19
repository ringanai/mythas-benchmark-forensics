# MYTHAS - Fiche audit: GSM8K

## Identite
- **Nom**: GSM8K
- **Famille**: math
- **Source primaire**: https://arxiv.org/abs/2110.14168 + https://github.com/openai/grade-school-math
- **Date de creation**: 2021-10

## Acces au test
- **Test public**: oui - prouve
- **Detail acces**: prouve - repo public avec fichiers `train.jsonl` et `test.jsonl`; le repo est archive mais toujours lisible
- **Mirrors connus**: prouve - Hugging Face, forks GitHub, nombreux blogs et jeux derives avec CoT ou variantes "socratic"

## Setup exact
- **Format**: open-ended math word problems
- **Nombre d'items**: prouve - environ 8.5K au total; 7.5K train et 1K test dans le repo officiel
- **Shots**: variable - 0-shot, few-shot et CoT sont tous utilises selon les papiers
- **Instructions**: libre - pas de system prompt prescrit

## Prompt regime
- **Prompt template**: prouve - pas de template unique impose; les implementations varient beaucoup
- **CoT**: variable - tres souvent utilise, parfois remplace par formats "socratic" ou solutions structurees
- **Parsing reponse**: prouve - extraction de la valeur numerique apres le token `####`
- **Sensibilite prompt mesuree**: a verifier - les sources primaires montrent surtout l'effet du verifier et du format de solution, pas une mesure canonique de prompt sensitivity

## Scoring
- **Metrique**: exact match sur la reponse numerique finale
- **Budget d'echantillonnage**: variable - la paper d'origine montre des gains importants avec generation de multiples solutions puis selection par verifier
- **Post-processing**: prouve - parsing de la valeur finale; annotations de calcul et calculators peuvent modifier le comportement de generation

## Version modele
- **Snapshot requis**: non - les scores sont souvent rapportes sans version precise
- **API vs weights**: mixte - API datees et weights publics selon les evals
- **Reproductibilite declaree**: plausible - le dataset est simple a lancer, mais verifier, budget, CoT et parsing rendent les comparaisons fragiles

## Contamination
- **Surface directe**: plausible - dataset public depuis 2021, largement miroir et repackage
- **Surface indirecte**: prouve - solutions completes, formats CoT, variantes socratic et distillations sont omnipresents
- **Mesures anti-contamination**: aucune - benchmark statique public sans test ferme ni decontamination explicite
- **Niveau de risque Mythas**: eleve

## Gaming
- **Prompt tuning**: plausible - few-shot et CoT benchmark-specifiques peuvent gonfler fortement le score
- **Format fitting**: prouve - le pattern `#### <nombre>` facilite l'extraction et le tuning sur le format de sortie
- **Hill-climbing**: plausible - benchmark largement suivi, avec forte incitation a iterer sur prompts et post-processing
- **Harness overfitting**: prouve - verifier, best-of-n et extraction numerique peuvent ameliorer le score sans mesurer une competence stable hors benchmark
- **Niveau de risque Mythas**: eleve

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: inutilisable (re-audit v0.5, 2026-04-19)
- **Verdict anterieur**: fragile (2026-04-19, pre-seuils v0.5)
- **Resume**: Benchmark historique important mais expose a la contamination et au format fitting. Les scores dependent beaucoup du regime CoT, du parsing et surtout du budget/verifier setup. Sous les seuils v0.5, toutes dimensions a 0 => inutilisable.
- **Date audit**: 2026-04-19

## Verdict v0.5 (re-audit 2026-04-19)
- **closure**: 0 (prouve) - repo OpenAI public depuis 2021-10, train + test + solutions detaillees tous accessibles, aucune partie fermee
- **contamination_direct**: 0 (prouve) - test set de 1000 items miroir sur HuggingFace, forks GitHub, blogs depuis 4+ ans, aucune decontamination
- **contamination_indirect**: 0 (prouve) - solutions CoT omnipresentes, variantes socratic / GSM-Symbolic / GSM-Hard, distillations CoT massives
- **incomparability**: 0 (prouve) - shots, prompt CoT, decoding, n_samples, verifier, parser: aucun canon
- **gaming_surface**: 0 (prouve) - 4+ categories (format fitting sur `####`, prompt tuning CoT, harness overfitting via verifier/best-of-n, hill-climbing)
- **governance**: 0 (prouve) - publie 2021-10, laisse en l'etat, repo archive, aucune rotation
- **s**: 0, **zeros**: 6
- **Verdict derive**: inutilisable
- **Reclassement**: fragile -> inutilisable
