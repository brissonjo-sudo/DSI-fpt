# Consignes de contribution — dépôt `dsi-fpt`

Ce dépôt porte un **skill d'aide à la décision**, pas une documentation. Ce qui
y est écrit est lu par un modèle et devient une réponse donnée à un directeur
des systèmes d'information. Les contraintes ci-dessous ne sont pas des
préférences de style.

## Contraintes non négociables

1. **Français** partout : contenu, commentaires de code, messages de commit.
2. **Aucune règle de droit, valeur ou délai de mémoire.** Seuils, délais,
   dates d'application, obligations : ils se vérifient à la source ou ne
   s'écrivent pas.
3. **Aucun identifiant Légifrance en dur** (`LEGIARTI`, `JORFTEXT`, `CETATEXT`)
   hors de `references/references-verifiees.md`, seul registre autorisé, et
   seulement pour des identifiants **réellement vérifiés**, datés.
4. **Applicabilité aux collectivités.** Une obligation qui vise l'État, ses
   opérateurs ou certaines entités seulement ne se présente jamais comme
   applicable à une collectivité sans la source qui l'établit. La doctrine
   (guides ANSSI, référentiels de l'État) n'est pas du droit positif.
5. **Les deux garde-fous sont intouchables.** Le garde-fou incident cyber et
   le garde-fou surveillance de personnes s'affichent **avant** tout contenu
   métier. Les affaiblir ou les rendre conditionnels est une régression
   bloquante.
6. **Les frontières sont opposables** : fond RGPD → `dpo-ct` ; fond statutaire
   et disciplinaire → `drh-fpt` ; autorisation et doctrine de vidéoprotection
   → `dpm-fpt` ; budget et montage financier → `dirfi-fpt` ; passation des
   marchés : hors périmètre. Une frontière ne s'illustre pas.
7. **Aucune donnée nominative**, ni secret, ni détail d'architecture réelle
   d'une collectivité identifiable, nulle part, y compris dans `JOURNAL.md`.
8. **Aucun mode opératoire offensif** : pas d'exploitation de vulnérabilité,
   pas de contournement de protection, pas de contre-attaque.
9. **Pas de duplication** : les branches pointent les unes vers les autres, les
   objets pointent vers les branches. Le même contenu n'existe qu'à un endroit.

## Décisions structurantes

Toute décision d'architecture (ajout d'une couche, déplacement d'une frontière,
changement de gabarit) fait l'objet d'une ADR dans `docs/adr/`.
