# Journal des cas — `dsi-fpt`

> Matière première de l'amélioration du skill. Une entrée par cas significatif :
> lacune constatée, erreur produite, cas nouveau non couvert, écrit récurrent à
> modéliser.
>
> **Règle stricte — aucune donnée nominative, aucun secret, aucun détail
> d'architecture réelle.** Ni agent, ni élu, ni usager, ni nom de collectivité,
> ni prestataire identifiable, ni adresse, ni plan de réseau, ni configuration.
> Anonymiser à l'écriture, pas après.
>
> Les entrées traitées remontent vers `CHANGELOG.md` à la montée de version.

## Format d'une entrée

```
### AAAA-MM-JJ — [titre court]

- **Type** : lacune | erreur | cas nouveau | écrit récurrent
- **Branche** : [fichier de references/ ou objets/ concerné]
- **Contexte (anonymisé)** : [situation, sans aucun élément identifiant]
- **Constat** : [ce que le skill a fait, ou n'a pas su faire]
- **Action proposée** : [modification envisagée, et où]
- **Statut** : à traiter | intégré vX.Y.Z
```

---

## Entrées

### 2026-10-05 — Création du skill

- **Type** : cas nouveau
- **Branche** : ensemble du skill
- **Contexte (anonymisé)** : la famille `collectivite-territoriale` n'avait
  aucun skill pour la mise en œuvre technique du SI ; `dpo-ct` renvoyait déjà
  vers un « futur skill DSI ».
- **Constat** : risque principal identifié au cadrage, importer comme
  obligations des collectivités des textes et doctrines qui visent l'État.
- **Action proposée** : colonne d'applicabilité dans le socle, réflexe
  « applicabilité d'abord », cas de test critique dédié.
- **Statut** : intégré v0.1.0
