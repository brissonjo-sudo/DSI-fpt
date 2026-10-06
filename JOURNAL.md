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

### 2026-10-06 — Portage de la campagne vers le poste de mesure

- **Type** : lacune
- **Branche** : outillage de mesure
- **Contexte (anonymisé)** : CLI connectée mais bloquée avant appel modèle
  dans l'environnement de préparation ; mesure locale demandée.
- **Constat** : un kit doit préserver les entrées séparées, figer le runtime
  et permettre la reprise sans mélanger modèles ou preuves.
- **Action proposée** : exporter un kit Claude/Codex avec lanceur séquentiel,
  traces brutes et preuves contrôlées ; documenter les limites d'isolation.
- **Statut** : intégré à l'outillage v0.2.0 ; aucune mesure réelle exécutée.

### 2026-10-05 — Reprise de rédaction et séparation des preuves

- **Type** : lacune
- **Branche** : ensemble du skill et outillage de mesure
- **Contexte (anonymisé)** : rédaction interrompue après le routeur ; aucun
  contenu métier complet ni campagne de mesure disponible.
- **Constat** : un dossier préparé ou un score logiciel ne doit pas être
  présenté comme mesure comportementale ; le titre de version seul ne
  rattache pas la preuve aux branches effectivement lues.
- **Action proposée** : achever les fichiers du cadrage, empreinter le runtime,
  figer le barème et relier chaque jugement à sa réponse ; séparer seuil,
  relecture praticien et publication.
- **Statut** : intégré v0.2.0 ; mesure et revue encore à conduire.

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
