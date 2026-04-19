# MYTHAS - Fiche audit: MMLU

## Identite
- **Nom**: MMLU (Massive Multitask Language Understanding)
- **Famille**: knowledge
- **Source primaire**: https://arxiv.org/abs/2009.03300 + https://github.com/hendrycks/test
- **Date de creation**: 2020-09

## Acces au test
- **Test public**: oui — prouve
- **Detail acces**: prouve — code d'eval, test set, dev set, val set tous publics sur GitHub
- **Mirrors connus**: prouve — HuggingFace (cais/mmlu, lukaemon/mmlu, etc.), nombreux forks GitHub, blogs avec solutions detaillees

## Setup exact
- **Format**: MCQ 4 choix (A/B/C/D)
- **Nombre d'items**: prouve — 15908 items test, 57 sujets
- **Shots**: variable — 0-shot et 5-shot utilises selon les papiers
- **Instructions**: libre — pas de system prompt prescrit

## Prompt regime
- **Prompt template**: prouve — pas de template unique impose; les implementations varient
- **CoT**: variable — certains rapportent avec CoT, d'autres sans
- **Parsing reponse**: variable — regex sur lettre, logprobs, generation libre puis extraction
- **Sensibilite prompt mesuree**: prouve — MMLU-Pro rapporte ~4-5% de variation sur MMLU selon le style de prompt (24 styles testes)

## Scoring
- **Metrique**: accuracy
- **Budget d'echantillonnage**: generalement 1 tentative (greedy), mais pas toujours specifie
- **Post-processing**: variable — certains utilisent logprobs, d'autres generation + parsing

## Version modele
- **Snapshot requis**: non — les scores sont souvent rapportes sans version precise
- **API vs weights**: mixte — API datees et weights publics, selon le modele
- **Reproductibilite declaree**: plausible — le benchmark est simple a lancer mais les details de prompt, parsing et version rendent la comparaison fragile

## Contamination
- **Surface directe**: plausible — items publics depuis 2020, largement indexes et repris
- **Surface indirecte**: plausible — solutions, walkthroughs, blogs, repos tiers omnipresents
- **Mesures anti-contamination**: aucune — benchmark statique public sans decontamination
- **Niveau de risque Mythas**: critique

## Gaming
- **Prompt tuning**: plausible — format MCQ simple, facilement optimisable par prompt
- **Format fitting**: plausible — pattern A/B/C/D tres reconnaissable, memorisation de templates probable
- **Hill-climbing**: plausible — scores publics sur leaderboards, incitation a optimiser iterativement
- **Harness overfitting**: plausible — les differences de harness (lm-eval, HELM, custom) produisent des scores differents pour le meme modele
- **Niveau de risque Mythas**: eleve

## Verdict Mythas
- **Statut audit**: audite
- **Verdict**: inutilisable (re-audit v0.5, 2026-04-19)
- **Verdict anterieur**: compromis (2026-04-19, pre-seuils v0.5)
- **Resume**: Benchmark canonique mais surface de contamination critique et non-comparabilite des scores documentee. Sous les seuils v0.5, toutes dimensions a 0 => inutilisable. Utile comme reference historique, pas comme ancre de score.
- **Date audit**: 2026-04-19

## Verdict v0.5 (re-audit 2026-04-19)
- **closure**: 0 (prouve) - items et labels telechargeables depuis 2020 via `hendrycks/test`
- **contamination_direct**: 0 (prouve) - aucune decontamination officielle; existence meme de MMLU-CF atteste de la severite
- **contamination_indirect**: 0 (prouve) - solutions, walkthroughs, miroirs HF, distillations omnipresents
- **incomparability**: 0 (prouve) - plusieurs harnesses coexistent; HELM documente les divergences
- **gaming_surface**: 0 (prouve) - 5+ categories applicables hors contamination directe
- **governance**: 0 (prouve) - aucun mecanisme de soumission tierce, pas de rotation
- **s**: 0, **zeros**: 6
- **Verdict derive**: inutilisable
- **Reclassement**: compromis -> inutilisable
