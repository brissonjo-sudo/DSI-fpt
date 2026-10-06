# Branche — Sécurité du SI

> Couche 2, lue après le routeur `references/analyse-situation.md`. Aucun
> identifiant officiel ni aucune valeur ici : les textes sont cités par leur
> objet, « à confirmer en version consolidée » ; leur identification est au
> registre `references/references-verifiees.md`. Toute valeur (délai, durée,
> date, version) : à vérifier à la source, voir `references/cache-valeurs.md`
> et `references/references-verifiees.md`.

## 1. Périmètre / Exclusions

**Périmètre.** Les mesures de sécurité du SI de la collectivité : politique de
sécurité (PSSI), analyse de risques, comptes et droits, authentification,
sauvegardes, mises à jour, postes et usages, journalisation, sensibilisation,
audits, homologation et attestation formelle de sécurité. La branche dit qui
décide, ce que la DSI exécute, et ce que la collectivité exige d'un service
mutualisé ou d'un prestataire.

**Exclusions.**
- **Incident en cours ou récent** → garde-fou `SKILL.md` §5.2, **avant tout
  contenu**, puis `references/crise-cyber-continuite.md` et
  `objets/incident-securite.md`.
- **Accès aux contenus ou aux traces d'une personne** (messagerie, fichiers,
  historique, journaux nominatifs, activité d'un poste) → garde-fou
  `SKILL.md` §5.3 et bascules, **sans mode opératoire**.
- **Droit des données personnelles** (exigences de conformité, niveau de
  risque pour les personnes, durée de conservation, information, AIPD,
  violation) → `BASCULE dpo-ct` (`SKILL.md` §5.5).
- **Adoption et opposabilité d'une charte, sanction d'un agent, télétravail
  au sens statutaire** → `BASCULE drh-fpt` (`SKILL.md` §5.6).
- **Vidéoprotection** : réseau, stockage et sécurité des équipements ici ;
  autorisation, doctrine d'emploi, exploitation → `BASCULE dpm-fpt`.
- Rôle, positionnement et désignation du RSSI → `references/gouvernance-strategie.md`.
- Architecture réseau, sites, parc → `references/infrastructures-reseaux.md`.
- Choix d'hébergement, qualification d'une offre en ligne → `references/cloud-hebergement.md`.
- Rédaction et exécution des clauses de sécurité → `references/contrats-prestataires.md`.
- Saisine électronique, identification des usagers → `references/dematerialisation-teleservices.md`.
- Budget de la sécurité → `BASCULE dirfi-fpt`. Passation : hors périmètre.

---

## 2. Questions couvertes

- « Par quoi commencer une PSSI ? »
- « Qui homologue un système, quand, et sur quel dossier ? »
- « L'ANSSI doit-elle valider notre homologation ? »
- « Sommes-nous soumis à NIS2 ? »
- « Le guide d'hygiène de l'ANSSI est-il obligatoire ? »
- « Que faire des comptes d'un agent qui part ? »
- « Comment organiser les sauvegardes pour résister à un rançongiciel ? »
- « Quels journaux tenir, et qui peut les consulter ? »
- « Peut-on lancer une campagne de faux hameçonnage ? »
- « Peut-on commander un test d'intrusion ? »
- « Que doit-on exiger de notre syndicat informatique ou de notre
  prestataire en matière de sécurité ? »

---

## 3. Arbre de traitement

`question → incident en cours ? (STOP §5.2) → une personne est-elle visée ?
(STOP §5.3) → frontière ? (BASCULE) → mode d'exercice (§4) → sous-domaine
(§5) → obligation ou bonne pratique, et applicabilité (§5.1, §5.2) → qui
décide, qui exécute, qui exige (§5.3) → vérification (§7, §9) → livrable
(§10)`

**Réflexes.**
- Classer chaque mesure : **obligation** (texte qui vise la collectivité) ou
  **bonne pratique** (doctrine). Ne jamais écrire « doit » sans le texte.
- Partir des **services publics à protéger**, pas des outils.
- En mode mutualisé ou externalisé, répondre **aussi** à la question : « que
  la collectivité exige-t-elle, contrôle-t-elle et conserve-t-elle ? ».
- Dès qu'une mesure observe des personnes, s'arrêter et appliquer le
  garde-fou §5.3.

---

## 4. Variables à lever

- **Mode d'exercice** (`SKILL.md` §2.4) :
  - *internalisé* : la DSI conçoit et exécute ; l'exécutif décide ;
  - *mutualisé* : lire la convention (service commun, syndicat, centre de
    gestion) ; distinguer ce que décide la collectivité et ce qu'exécute le
    service mutualisé ;
  - *externalisé* : lister ce que le contrat permet d'exiger et de contrôler.
- **Catégorie de la collectivité** : utile seulement si un texte en dépend
  (suivi de la transposition de NIS2, §5.1). Pas de seuil de taille pour la
  sécurité en général.
- **Système concerné** : téléservice ouvert aux usagers, application
  métier, messagerie, poste de travail, sauvegardes, équipements de site.
- **Nature et sensibilité des données** : données personnelles, données de
  personnes vulnérables, données de santé ou sociales. Si oui, prévoir la
  `BASCULE dpo-ct` pour les exigences.
- **Criticité du service** : interruption tolérable, mode dégradé possible ou
  non.
- **Existant** : PSSI, analyse de risques, attestation formelle déjà
  signée, dernier réexamen, cartographie, inventaire des comptes.
- **Prestataire et contrat** : clauses de sécurité, accès aux journaux,
  sauvegardes, audit, réversibilité.
- **Date de référence** : versions des référentiels et état de la
  transposition de NIS2 à la date de la question.

Si le mode d'exercice change la réponse et n'est pas donné, le demander.

---

## 5. Règles métier

### 5.1 Ce qui oblige la collectivité

**Référentiel général de sécurité (RGS)** — registre §4 et §15.1.
- L'ordonnance relative aux échanges électroniques entre les usagers et les
  autorités administratives définit les « autorités administratives » en
  nommant **expressément les collectivités territoriales**. C'est le
  fondement de l'applicabilité.
- L'autorité qui met en place un système d'information en détermine les
  fonctions de sécurité et respecte le RGS (ordonnance, à confirmer en
  version consolidée).
- Le décret relatif au RGS impose une **analyse de risques**, la définition
  d'**objectifs et de fonctions de sécurité**, et leur **réexamen régulier**.
  Applicabilité : par renvoi à la définition de l'ordonnance (le registre la
  qualifie d'inférence).
- Le même décret prévoit le recours à des produits et prestataires
  **qualifiés ou conformes** ; portée exacte à confirmer en version
  consolidée.
- Le décret prévoit que l'autorité administrative **atteste formellement**
  la sécurité de son système ; pour un téléservice, cette attestation est
  **rendue accessible aux usagers**.
- Le **référentiel** RGS, approuvé par arrêté, décrit la démarche sous le nom
  d'**homologation de sécurité**. La page de l'ANSSI qui le présente cite
  expressément les collectivités ; elle présente la démarche d'homologation
  et l'analyse de risques comme exigées, le reste comme recommandations.
- **Qui homologue et atteste** : la collectivité, pour ses propres systèmes.
  L'ANSSI **qualifie des produits** ; elle n'homologue pas les systèmes d'une
  collectivité.
- Champ exact des systèmes soumis, articles du décret non relus au registre,
  arrêté d'approbation : **à vérifier** (registre §4).

**Code pénal, atteintes aux systèmes de traitement automatisé de données** —
registre §6.
- Ces incriminations protègent les systèmes de la collectivité : elles
  fondent une plainte de la collectivité victime.
- Elles s'appliquent aussi à un agent ou à un prestataire auteur.
- La détention d'outils d'attaque est réprimée sauf **motif légitime**,
  notamment de recherche ou de sécurité informatique : c'est ce qui couvre un
  audit ou un test commandé et cadré (§5.11).
- Aggravations propres aux systèmes de l'État : elles ne visent pas la
  collectivité.

**NIS2** — registre §8.
- La directive n'est **pas transposée** à la date du registre. Elle laisse
  l'administration publique locale à l'**option** de chaque État.
- **Ne jamais écrire** que la collectivité « est soumise à NIS2 ».
- Écrire : « à suivre ; l'applicabilité dépendra de la loi de transposition
  et de ses critères, à vérifier à la date de la question ».
- La collectivité peut **anticiper** des mesures de la directive à titre de
  bonne pratique, en le disant.

**Sécurité des traitements de données personnelles** — registre §14.
- Le régime du RGPD relatif à la sécurité du traitement relève de `dpo-ct`.
  La DSI choisit et déploie les mesures ; `dpo-ct` fixe les exigences.

### 5.2 Ce qui relève de la bonne pratique

- **Guide d'hygiène informatique** (ANSSI) : bonne pratique. Aucun texte ne
  le rend obligatoire (registre §15.2).
- **EBIOS Risk Manager** (ANSSI) : méthode d'analyse de risques **au libre
  choix** de la collectivité. Le décret impose une analyse de risques, pas
  cette méthode.
- **Guides ANSSI destinés aux collectivités** (avec l'AMF ; synthèse
  réglementaire) : bonne pratique ; guides datés, à croiser avec le droit en
  vigueur.
- **PSSI** : aucun texte du registre n'impose ce document sous ce nom. C'est
  le véhicule naturel des objectifs et fonctions de sécurité exigés par le
  RGS. Le présenter ainsi.
- Citer toute doctrine avec sa version et sa date, et la mention
  « doctrine, non normative ».

### 5.3 Qui décide, qui exécute, qui exige

| Acte | Décide | Exécute | Exige ou contrôle |
|---|---|---|---|
| PSSI | Exécutif (signature) | DSI ou RSSI (rédaction, déploiement) | `dpo-ct` pour les données personnelles |
| Analyse de risques | Exécutif (acceptation des risques résiduels) | DSI ou RSSI, métiers | — |
| Attestation formelle / homologation | Autorité administrative : la collectivité (signataire exact à vérifier selon les délégations) | DSI : dossier | Commission ou autorité d'homologation désignée par la collectivité |
| Mesures techniques | DSI dans le cadre fixé | DSI, service mutualisé ou prestataire | RSSI ; `dpo-ct` pour les exigences |
| Charte d'usage | Adoption → `drh-fpt` | DSI : contenu technique | — |

### 5.4 Homologation et attestation formelle

- **Avant mise en service** d'un système, en particulier d'un téléservice.
- **À chaque évolution significative** et au **réexamen régulier** prévu par
  le décret.
- **Dossier** : périmètre du système, analyse de risques, mesures retenues,
  risques résiduels, plan d'action, résultats d'audit s'il y en a.
- **Décision** : l'autorité de la collectivité accepte les risques résiduels
  et atteste. La DSI **prépare** ; elle ne signe pas à la place de
  l'exécutif, sauf délégation établie.
- **Mode mutualisé ou externalisé** : la collectivité atteste pour ses
  systèmes, même hébergés ailleurs. Elle exige du service mutualisé ou du
  prestataire les éléments du dossier (description, mesures, audits). La
  répartition de l'attestation pour un système partagé se lit dans la
  convention ; **à vérifier**.
- Gabarit : `references/templates/note-homologation.md`.

### 5.5 Comptes, droits et authentification

- **Comptes nominatifs** ; comptes partagés proscrits ou tracés.
- **Moindre privilège** : chaque droit se justifie par une mission.
- **Comptes d'administration distincts** des comptes de bureautique.
- **Authentification renforcée** pour l'administration et les accès
  distants.
- **Revue périodique** des droits, fréquence fixée par la PSSI.
- **Arrivée, mobilité, départ** : processus déclenché par une information
  fiable du service RH ; désactivation à la date de départ ; retrait des
  droits devenus inutiles à la mobilité. Voir `objets/compte-poste-agent.md`.
- **Données d'un agent parti ou absent** (messagerie, fichiers) : demande de
  surveillance au sens du routeur → **garde-fou §5.3**, `BASCULE dpo-ct` et
  `BASCULE drh-fpt`. Ne décrire ni l'accès ni l'extraction.
- **Comptes de prestataires** : nominatifs, limités dans le temps et le
  périmètre, tracés, retirés en fin d'intervention.

### 5.6 Sauvegardes

- Au moins une copie **isolée** du système de production, hors d'atteinte
  d'un compte compromis.
- **Tests de restauration** réguliers, documentés. Une sauvegarde jamais
  restaurée n'est pas une garantie.
- **Périmètre** écrit : quels systèmes, quelles données, quel ordre de
  restauration (lien avec le PRA : `references/crise-cyber-continuite.md`).
- **Mode externalisé** : exiger la preuve des tests de restauration, la
  localisation des copies et la capacité à les récupérer.
- Durée de conservation des données personnelles sauvegardées → `BASCULE
  dpo-ct`.

### 5.7 Mises à jour et obsolescence

- Tenir un **inventaire** des systèmes et de leur fin de support.
- Prioriser selon l'**exposition** (services ouverts sur internet d'abord)
  et la criticité.
- Un système sans support se traite comme un **risque résiduel** accepté par
  écrit, ou se remplace.
- Mode externalisé : le maintien en condition de sécurité se prévoit au
  contrat (`references/contrats-prestataires.md`).

### 5.8 Postes et usages

- Configuration de référence durcie, protection contre les codes
  malveillants, chiffrement des équipements mobiles.
- Règles sur les supports amovibles et les équipements personnels.
- Télétravail : équipement et accès distants ici ; organisation et statut →
  `BASCULE drh-fpt`.
- Règles d'usage : contenu technique de la charte →
  `references/templates/charte-usage-si.md`.

### 5.9 Journalisation

- **Ce qui relève de la branche** : décider quels événements de sécurité
  journaliser, protéger l'intégrité des journaux, en restreindre l'accès,
  **tracer l'accès aux journaux eux-mêmes**.
- **Finalité** : détection et analyse d'incidents de sécurité.
- **Durée de conservation, information des agents, base légale** → `BASCULE
  dpo-ct`.
- **Consultation nominative** (rechercher ce qu'a fait un agent) →
  **garde-fou §5.3**. Décrire ce qu'il faudra exiger et tracer, jamais
  comment extraire.
- Mode externalisé ou mutualisé : exiger l'**accès** aux journaux de sécurité
  et leur **conservation** dans les conditions fixées.

### 5.10 Sensibilisation

- Bonne pratique : programme régulier, adapté aux métiers et aux élus.
- **Simulation d'hameçonnage** : exploiter des résultats **agrégés**.
  Résultats nominatifs ou suite individuelle → **garde-fou §5.3**, `BASCULE
  dpo-ct` et `BASCULE drh-fpt`.

### 5.11 Audits et tests

- Un test se **commande par écrit** : autorité signataire, périmètre, dates,
  prestataire, règles d'engagement. C'est ce cadre qui établit le motif
  légitime (§5.1).
- **Jamais** de test d'un système tiers, y compris celui d'un prestataire ou
  d'un service mutualisé, sans son accord écrit.
- Prestataire : vérifier sa **qualification** au catalogue de l'ANSSI à la
  date de la décision, si la collectivité la retient comme exigence.
- Résultats : diffusion restreinte ; jamais de détail exploitable dans un
  écrit largement diffusé.

### 5.12 Mode d'exercice : ce que la collectivité exige

| Exigence | Mutualisé | Externalisé |
|---|---|---|
| Responsabilité | Reste à la collectivité ; la convention répartit l'exécution | Reste à la collectivité ; le contrat fixe les obligations du prestataire |
| Documents de sécurité | Accès à la PSSI du service et à ses analyses de risques | Plan d'assurance sécurité, résultats d'audit |
| Journaux | Accès aux journaux de sécurité qui la concernent | Idem, prévu au contrat |
| Sauvegardes | Preuve des tests de restauration | Idem, et localisation des copies |
| Alerte | Information sans délai de tout incident la concernant | Idem, délai fixé au contrat |
| Comptes | Revue des comptes ayant accès à ses données | Idem |
| Homologation | Éléments du dossier fournis par le service | Idem |
| Réversibilité | Restitution des données et de la documentation | Idem (`references/contrats-prestataires.md`) |

Mutualisation entre un EPCI à fiscalité propre et ses communes : service
commun par convention, sous conditions (registre §9). Autres formes
(syndicat, centre de gestion) : lire l'acte qui les fonde.

---

## 6. Procédures

### 6.1 Bâtir une première PSSI

Hypothèse : aucune PSSI en vigueur.
1. Obtenir le **mandat** de l'exécutif ou du DGS.
2. Lever le **mode d'exercice** et réunir conventions et contrats.
3. Établir la **cartographie** : services publics, applications, données,
   prestataires.
4. Conduire l'**analyse de risques** (méthode au choix ; EBIOS RM possible).
5. Fixer les **objectifs** et les **mesures**, par priorité.
6. Faire **valider** par l'exécutif, avec les risques résiduels.
7. Recueillir les exigences de `dpo-ct` sur les données personnelles.
8. Décliner en règles d'usage (charte : contenu technique ici, adoption →
   `drh-fpt`).
9. Fixer le **réexamen** (fréquence à décider, et après tout incident
   majeur).

Point de contrôle : chaque mesure est classée obligation ou bonne pratique.

### 6.2 Homologuer un système

1. Délimiter le système et son mode d'exercice.
2. Désigner l'autorité qui attestera (signataire et délégation à vérifier).
3. Analyse de risques ; mesures ; risques résiduels.
4. Audit si le niveau de risque le justifie.
5. Dossier et note d'homologation (`references/templates/note-homologation.md`).
6. Décision et attestation formelle par l'autorité.
7. Pour un téléservice : rendre l'attestation accessible aux usagers.
8. Planifier le réexamen.

Données manquantes : produire un brouillon `[INCOMPLET]`.

### 6.3 Revue des comptes et des droits

1. Extraire la **liste des comptes** et leurs droits (inventaire
   d'administration, pas consultation d'activité).
2. Confronter à la liste des agents et des prestataires fournie par les
   services compétents.
3. Faire valider les droits par chaque responsable de service.
4. Retirer l'inutile ; tracer la revue.

Toute question sur **l'activité** d'un compte nominatif → garde-fou §5.3.

---

## 7. Déclencheurs de vérification

Appliquer `references/socle-sources-verification.md` dès que la réponse
porte sur :
- une **obligation** de la collectivité en matière de sécurité ;
- l'**applicabilité** d'un texte : RGS, transposition de NIS2, texte
  sectoriel ;
- la **compétence** : qui atteste, qui signe, délégation ;
- la **version** d'un référentiel (RGS, EBIOS RM, guide d'hygiène) ;
- la **qualification** d'un produit ou d'un prestataire, à la date de la
  décision ;
- l'**état de la transposition** de NIS2 ;
- une **qualification pénale** ou une plainte → `recherche-juridique` ;
- toute **durée** de conservation, toute **fréquence** présentée comme
  imposée.

---

## 8. Pièges et confusions fréquentes

1. **« La collectivité est soumise à NIS2. »** Faux à la date du registre :
   directive non transposée, niveau local en option nationale.
2. **Confondre les deux niveaux du RGS** : le décret parle d'**attestation
   formelle** ; le référentiel, d'**homologation de sécurité**. Employer le
   bon terme au bon niveau.
3. **« L'ANSSI homologue notre système. »** Faux : la collectivité atteste ;
   l'ANSSI qualifie des produits.
4. **Présenter le guide d'hygiène ou EBIOS RM comme obligatoires.** Ce sont
   des bonnes pratiques.
5. **Importer une doctrine de l'État** (doctrine « cloud au centre »,
   exigences propres aux administrations de l'État) comme obligation de la
   collectivité.
6. **Relayer le renvoi du décret RGS vers le CRPA** pour la décision de
   créer un téléservice : le registre signale que l'article visé ne traite
   plus cet objet. Ne pas le relayer.
7. **« Le prestataire est responsable de la sécurité. »** La collectivité
   reste responsable ; elle exige et contrôle.
8. **Surveillance déguisée** : « récupérer les mails d'un agent absent »,
   « voir qui a consulté ce dossier », « mesurer l'activité d'un poste »,
   « résultats nominatifs du faux hameçonnage » → garde-fou §5.3.
9. **Traiter ici la durée de conservation des journaux** : elle relève de
   `dpo-ct`.
10. **Confondre audit commandé et test d'un système tiers** : le second,
    sans accord écrit, relève des atteintes pénales.
11. **Donner un détail d'architecture** dans une PSSI ou une note diffusée
    largement.
12. **Citer une version de référentiel de mémoire.**

---

## 9. Données et valeurs à vérifier

Aucune valeur n'est écrite ici. Délai/valeur à vérifier à la source : voir
`cache-valeurs.md` et `references-verifiees.md`.
- **Versions** du référentiel RGS et de ses annexes, d'EBIOS RM, du guide
  d'hygiène.
- **Champ exact** des systèmes soumis au RGS et articles du décret non relus
  au registre.
- **Arrêté** d'approbation du RGS et délais transitoires éventuels.
- **État de la transposition de NIS2**, critères d'inclusion des
  collectivités, date d'application.
- **Peines** prévues par le code pénal pour les atteintes aux systèmes.
- **Qualification** d'un produit ou d'un prestataire, au catalogue de
  l'ANSSI à la date de la décision.
- **Délégation de signature** de l'attestation formelle dans la collectivité.
- Toute **durée** de conservation des journaux et des sauvegardes → `dpo-ct`.

Références structurelles, citables avec la réserve « à confirmer en version
consolidée » : ordonnance relative aux échanges électroniques ; décret relatif
au RGS ; code pénal, atteintes aux systèmes de traitement automatisé de
données (registre §4, §6).

---

## 10. Écrits et livrables

- **PSSI** : objectifs, périmètre, rôles, mesures par sous-domaine, réexamen.
  Classer chaque règle obligation / bonne pratique. Aucun secret, aucun
  détail d'architecture.
- **Note d'homologation** : `references/templates/note-homologation.md`.
  Éléments : système, analyse de risques, risques résiduels, décision,
  signataire, date de réexamen.
- **Charte d'usage du SI** (contenu technique) :
  `references/templates/charte-usage-si.md` ; adoption → `drh-fpt`.
- **Cahier des charges technique** (exigences de sécurité d'un achat) :
  `references/templates/cahier-des-charges-technique.md`.
- **Procédure de gestion des comptes** : arrivée, mobilité, départ, revue.
- Pilotage des écrits : `references/ecrits-numerique.md`. Données
  manquantes : brouillon `[INCOMPLET]`.

---

## 11. Double échelle [risque / confiance]

| Sous-domaine | Risque | Confiance |
|---|---|---|
| PSSI, bonnes pratiques d'hygiène | Moyen | Stable sur la méthode |
| Applicabilité du RGS | Élevé | Stable sur le principe ; à vérifier sur le champ exact |
| Attestation formelle d'un téléservice | Élevé | Stable sur le principe ; à vérifier sur le signataire |
| NIS2 et collectivités | Élevé | À vérifier ; abstention sur toute obligation |
| Comptes d'un agent qui part | Moyen ; élevé si accès à ses contenus (§5.3) | Stable sur la technique |
| Sauvegardes | Élevé (continuité du service public) | Stable |
| Journalisation | Moyen ; critique si consultation nominative (§5.3) | Stable sur la technique ; durées → `dpo-ct` |
| Audit et test d'intrusion | Élevé | Stable sur le cadrage écrit |
| Exigences envers un prestataire | Moyen à élevé | Stable sur le principe ; contrat à lire |

---

## 12. Checklist de branche

1. **Incident en cours ou récent ?** Si oui, le STOP de `SKILL.md` §5.2
   est-il en premier ?
2. **Personne visée** (messagerie, fichiers, journaux nominatifs, activité
   d'un poste, résultats nominatifs) ? Si oui, STOP §5.3 et bascules avant
   tout contenu, **sans mode opératoire** ?
3. **Mode d'exercice** levé, et exigences envers le service mutualisé ou le
   prestataire énoncées ?
4. Chaque « doit » repose-t-il sur un texte qui **vise la collectivité**,
   avec la raison de l'applicabilité ?
5. **NIS2** présentée comme non transposée et à suivre, jamais comme
   applicable ?
6. **Vocabulaire RGS** exact : attestation formelle (décret), homologation
   de sécurité (référentiel), collectivité qui atteste, ANSSI qui qualifie
   des produits ?
7. Guide d'hygiène et EBIOS RM présentés comme **bonne pratique** ?
8. Aucune **valeur** (version, durée, délai, peine) écrite de mémoire ?
9. Aucun **identifiant officiel** hors du registre ?
10. Exigences de conformité, durées de conservation, violation → `BASCULE
    dpo-ct` au format de `SKILL.md` §5.5, `dpo-ct` nommé ?
11. Charte, sanction, télétravail → `BASCULE drh-fpt` ; vidéoprotection →
    `BASCULE dpm-fpt` ?
12. Aucun secret, aucun détail d'architecture exploitable, aucun mode
    opératoire offensif ?
13. Chaque fichier mobilisé nommé par son **chemin** ?
14. Couple **[risque / confiance]** indiqué quand utile ?
15. Cas journalisable proposé pour `JOURNAL.md`, anonymisé ?
