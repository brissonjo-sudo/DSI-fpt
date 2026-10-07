# Note de transmission — frontière `dsi-fpt` / `dcp-fpt`

> **Destinataire** : la session qui reprend le skill `dsi-fpt`.
> **Origine** : dépôt `DCP-fpt`, `docs/frontiere-dsi-fpt.md` (2026-10-06),
> reprise ici le 2026-10-07 pour être lisible depuis ce dépôt.
> **Statut** : partage adopté par l'auteur.
> **État de `dcp-fpt`** : skill 0.1.0 rédigé et fusionné sur son `main`,
> **non mesuré, non relu par un praticien, pas encore distribué** (aucune
> intégration au plugin `collectivite-territoriale`).
> Cette note n'est **pas** appliquée dans ce dépôt : elle propose ce qu'il y a
> lieu d'y reporter. Son ajout ne modifie ni les fichiers du skill ni les
> branches en cours. Un renvoi depuis `AGENTS.md` est à votre main.

## Le partage

Pour un **achat informatique** (logiciel, hébergement, infogérance,
maintenance, télécoms) :

| Question | Skill compétent |
|---|---|
| Spécifications techniques du besoin, contenu technique du cahier des charges | `dsi-fpt` |
| Niveaux de service, réversibilité, restitution des données, licences, sécurité : **contenu technique** des clauses | `dsi-fpt` |
| Suivi technique de l'exécution, recette technique | `dsi-fpt` |
| Choix de la procédure, publicité, critères, analyse des offres, attribution | `dcp-fpt` |
| **Régime juridique** d'une modification du contrat (est-elle permise, sous quelle forme) | `dcp-fpt` |
| **Régime juridique** de la mise en demeure, de la résiliation, du contentieux | `dcp-fpt` |
| Choix du CCAG et dérogations | `dcp-fpt` |
| Avances, révision des prix, pénalités (calcul et imputation), paiement | `dirfi-fpt` |
| Clauses de sous-traitance des données personnelles | `dpo-ct` |

**Exemple** : « l'éditeur refuse de restituer nos données ».
- `dsi-fpt` dit **ce qu'il faut exiger** techniquement (formats, délais à
  vérifier dans le contrat, intégrité) et **ce que dit la clause** de
  réversibilité.
- `dcp-fpt` dit **comment le faire valoir** : mise en demeure, pénalités
  prévues (calcul → `dirfi-fpt`), résiliation, juge.

## Ce qu'il y aurait lieu de reporter dans `dsi-fpt`

1. **Fiche `contrats-prestataires`** (cadrage §6.10). Aujourd'hui, la passation
   y figure comme « hors périmètre », sans skill nommé.
   - Remplacer par `BASCULE dcp-fpt` une fois `dcp-fpt` publié.
   - Restreindre la mention « code de la commande publique (exécution et
     modification des contrats) » au **contenu des clauses**.
   - Renvoyer le **régime juridique** des modifications et de la résiliation à
     `dcp-fpt`.
2. **Frontière « Achat informatique »** (cadrage §4, `SKILL.md` §5.6) :
   remplacer « Passation : hors périmètre » par `dcp-fpt`, **seulement quand
   `dcp-fpt` est distribué**. D'ici là, garder « hors périmètre » : un renvoi
   vers un skill inexistant est un pointeur mort.
3. **Cas de test 27** de `dsi-fpt` (choisir la procédure de passation d'un
   logiciel) : l'attendu « hors périmètre, signaler » reste valable tant que
   `dcp-fpt` n'est pas distribué.
