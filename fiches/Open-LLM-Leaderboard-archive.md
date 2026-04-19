# MYTHAS - Fiche audit: Open LLM Leaderboard archive

## Identite
- **Nom**: Open LLM Leaderboard v1 (archive)
- **Famille**: leaderboard
- **Source primaire**: https://huggingface.co/docs/leaderboards/open_llm_leaderboard/archive + https://huggingface.co/blog/open-llm-leaderboard-mmlu
- **Date de creation**: 2023

## Acces au test
- **Test public**: oui - prouve
- **Detail acces**: prouve - setup documente publiquement, resultats / requests datasets publics, reproduction possible via une version precise du EleutherAI LM Evaluation Harness
- **Mirrors connus**: prouve - docs Hugging Face, Space archivee, datasets `open-llm-leaderboard-old/results` et `open-llm-leaderboard-old/requests`

## Setup exact
- **Format**: leaderboard agregeant une batterie fixe de benchmarks publics
- **Nombre d'items**: prouve - pas un test set unique; combinaison de 6 benchmarks historiques (ARC, HellaSwag, MMLU, TruthfulQA, Winogrande, GSM8K) avec few-shot counts fixes
- **Shots**: prouve - regles figees par benchmark (par ex. ARC 25-shot, HellaSwag 10-shot, MMLU 5-shot, TruthfulQA 0-shot, Winogrande 5-shot, GSM8K 5-shot)
- **Instructions**: prouve - benchmark prompts definis par le harness / les taches sous-jacentes, pas par un protocole conversationnel libre

## Prompt regime
- **Prompt template**: prouve - derive du LM Evaluation Harness et des implementations des benchmarks sous-jacents
- **CoT**: variable - a verifier - la documentation archivee expose surtout le regime harness fixe, pas une politique unique de CoT pour toutes les taches
- **Parsing reponse**: prouve - metriques benchmark-specifiques agregees ensuite en score leaderboard normalise
- **Sensibilite prompt mesuree**: prouve - indirectement documentee par Hugging Face via l'analyse MMLU, qui montre que des implementations/promptings differents changent materialement les scores et le ranking

## Scoring
- **Metrique**: prouve - aggregation de scores benchmark-specifiques avec normalisation 0-100 pour faciliter la comparaison
- **Budget d'echantillonnage**: prouve - batch size, revision du modele et version du harness comptent; la doc avertit d'ailleurs que le batch size peut faire legerement varier les resultats
- **Post-processing**: prouve - normalisation des scores, agregation cross-benchmark, affichage d'un score unique qui peut masquer des heterogeneites fortes

## Version modele
- **Snapshot requis**: prouve - la doc demande explicitement un `revision=<your_model_revision>` pour reproduire
- **API vs weights**: prouve - centré sur modeles open-source / chatbots open soumis a une evaluation standardisee
- **Reproductibilite declaree**: prouve - c'etait la promesse centrale du projet; toutefois la reproductibilite reste liee a une version precise du harness et des benchmarks sous-jacents

## Contamination
- **Surface directe**: prouve - la suite repose sur des benchmarks publics statiques et tres diffuses
- **Surface indirecte**: prouve - prompts optimises, eval tuning, selection de variantes et hill-climbing deviennent rationnels des lors que la batterie est connue et centrale
- **Mesures anti-contamination**: faible - prouve - la force du leaderboard est la standardisation, pas la decontamination
- **Niveau de risque Mythas**: eleve

## Gaming
- **Prompt tuning**: prouve - le projet est ne justement pour contrer les comparaisons injustes dues aux setups optimises; mais la batterie fixe reste une cible explicite de tuning
- **Format fitting**: prouve - l'agregation de six benchmarks encourages a optimiser ces formats plutot qu'une competence generalisable
- **Hill-climbing**: prouve - le leaderboard a ete retire en partie parce qu'il risquait d'encourager du hill-climbing sur des directions devenues peu pertinentes
- **Harness overfitting**: prouve - le billet MMLU montre qu'un meme benchmark change de valeur et d'ordre de classement selon l'implementation exacte
- **Niveau de risque Mythas**: critique

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: inutilisable (re-audit v0.5, 2026-04-19)
- **Verdict anterieur**: fragile (2026-04-19, pre-seuils v0.5)
- **Resume**: Utile comme anti-marketing layer historique. Sous v0.5, 5 zeros + s=1 => inutilisable comme ancre de score actuel; reste une borne publique avec avertissement.
- **Date audit**: 2026-04-19

## Verdict v0.5 (re-audit 2026-04-19)
- **closure**: 0 (prouve) - batterie de benchmarks publics fixes (MMLU, ARC, HellaSwag, TruthfulQA, Winogrande, GSM8K)
- **contamination_direct**: 0 (prouve) - tous les composants publics depuis plusieurs annees, aucun avec decontamination officielle
- **contamination_indirect**: 0 (prouve) - solutions, walkthroughs, datasets miroirs massivement indexes
- **incomparability**: 0 (prouve) - les auteurs documentent les divergences selon harness (ex MMLU lm-eval vs officiel)
- **gaming_surface**: 1 (prouve) - 3 categories majeures hors contamination directe (prompt_tuning, harness_overfitting, hill_climbing)
- **governance**: 0 (prouve) - leaderboard archive, figee, pas de re-release ni mecanisme tiers
- **s**: 1, **zeros**: 5
- **Verdict derive**: inutilisable (regle `zeros >= 5`)
- **Reclassement**: fragile -> inutilisable
