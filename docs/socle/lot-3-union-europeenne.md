# Socle de sources, lot 3 : droit de l'Union européenne

> Note de maintenance du 2026-10-05 : les identifiants officiels sont centralisés
> dans `../../references/references-verifiees.md`, conformément à AGENTS.md.
> Les mentions non retenues ne sont pas utilisables comme points d’entrée.
> La trace de travail d’origine reste dans le commit historique `ad3e4ee`.

- **Date de vérification** : 2026-10-05.
- **Méthode** : textes officiels en français récupérés sur **CELLAR**, le dépôt
  de l'Office des publications de l'Union européenne
  (`https://publications.europa.eu/resource/celex/<CELEX>`, en-têtes
  `Accept: application/xhtml+xml` et `Accept-Language: fra`). Le texte
  renvoyé est l'acte publié au Journal officiel, ou sa version consolidée
  quand le numéro CELEX consolidé est demandé. Les passages ont été extraits
  par recherche dans le texte, sans reformulation par un modèle.
- **Pourquoi pas EUR-Lex** : la lecture d'EUR-Lex a échoué. Le site renvoie un
  statut 202 au corps vide (défi anti-robot), ce qui explique l'échec d'une
  première passe faite par WebFetch, qui avait conclu à « 0 élément vérifié ».
  Cette passe est remplacée par celle-ci.
- **Rappel** : aucune référence de mémoire. Ce qui n'a pas été lu reste
  « ⚠️ non vérifié ».
- **Portée** : une version consolidée de l'Union « n'a aucun effet juridique »
  (avertissement figurant en tête du document) : la référence opposable reste
  l'acte de base et ses modificatifs, cités ci-dessous.

## Tableau

| Acte et article | Objet (une phrase) | Entrée en vigueur / application | Identifiant (CELEX) | Vérifié le | Statut | Applicable aux collectivités (oui/non/sous conditions + fondement) |
|---|---|---|---|---|---|---|
| Règlement (UE) 2024/1689 (IA), art. 3, point 4 | Définit le « déployeur ». | Voir art. 113 | voir registre vérifié | 2026-10-05 | vérifié | **Oui** : « une personne physique ou morale, une autorité publique, une agence ou un autre organisme utilisant sous sa propre autorité un système d'IA ». Une collectivité qui utilise un système d'IA est déployeur. |
| Règlement (UE) 2024/1689, art. 27 (version consolidée au 27/07/2026) | Impose une analyse d'impact sur les droits fondamentaux avant le déploiement de certains systèmes à haut risque. | Suit le calendrier du chapitre III (art. 113) | voir registre vérifié ; consolidé voir registre vérifié | 2026-10-05 | vérifié | **Oui, sous conditions** : vise « les déployeurs qui sont des organismes de droit public ou des entités privées fournissant des services publics », pour les systèmes à haut risque de l'art. 6 § 2, sauf ceux de l'annexe III point 2. |
| Règlement (UE) 2024/1689, annexe III, point 5 a) | Classe à haut risque les systèmes destinés à évaluer l'éligibilité aux prestations et services d'aide sociale essentiels. | Voir art. 113 | voir registre vérifié | 2026-10-05 | vérifié | **Oui, sous conditions** : vise les systèmes « utilisés par les autorités publiques ou en leur nom », par exemple pour octroyer, réduire ou révoquer une prestation. |
| Règlement (UE) 2024/1689, art. 113 (version consolidée au 27/07/2026) | Fixe l'entrée en vigueur et les dates d'application, telles que modifiées. | Date générale : 2 août 2026. Chapitres I et II : 2 février 2025 (certains points de l'art. 5 : 2 décembre 2026). Chapitre III, sections 1 à 3 : 2 décembre 2027 pour l'annexe III, 2 août 2028 pour l'annexe I. | consolidé voir registre vérifié | 2026-10-05 | vérifié | Calendrier commun ; voir la ligne suivante pour les autorités publiques. |
| Règlement (UE) 2026/1744 du 8 juillet 2026 (« omnibus numérique sur l'IA »), modifiant le règlement 2024/1689 | Modifie le calendrier et diverses obligations du règlement IA. | Publié au JOUE le 24 juillet 2026 | voir registre vérifié | 2026-10-05 | vérifié | **Oui, sous conditions** : la disposition modifiée prévoit que « les fournisseurs et les déployeurs de systèmes d'IA à haut risque destinés à être utilisés par des autorités publiques » se conforment « au plus tard le 2 août 2030 » pour les systèmes déjà en service. |
| Règlement (UE) 2024/1689, art. 5 (pratiques interdites) | Encadre notamment l'identification biométrique à distance en temps réel dans les espaces accessibles au public à des fins répressives, soumise à autorisation préalable d'une autorité judiciaire ou administrative indépendante. | Chapitres I et II : 2 février 2025 | voir registre vérifié | 2026-10-05 | vérifié (passage sur l'autorisation préalable) ; ⚠️ liste complète des interdictions non relue | **Sous conditions** : le régime répressif concerne les autorités répressives. Pour une collectivité, il sert de **frontière** (garde-fou §3.2 du cadrage et `dpm-fpt`), jamais de mode d'emploi. |
| Directive (UE) 2022/2555 (NIS2), art. 2 § 5 | Permet aux États membres d'étendre la directive aux entités de l'administration publique au niveau local. | — | voir registre vérifié | 2026-10-05 | vérifié | **Option nationale** : « Les États membres peuvent prévoir que la présente directive s'applique : a) aux entités de l'administration publique au niveau local ». L'applicabilité aux collectivités dépend de la loi française de transposition, **non publiée à cette date** (lot 2). |
| Directive (UE) 2022/2555, art. 41 | Fixe la transposition au 17 octobre 2024 et l'application au 18 octobre 2024. | — | voir registre vérifié | 2026-10-05 | vérifié | Sans effet direct sur les collectivités tant que la transposition n'est pas publiée (France en retard, lot 2). |
| Directive (UE) 2016/2102 (accessibilité des sites et applications du secteur public), art. 3, point 1 | Définit l'« organisme du secteur public ». | — | voir registre vérifié | 2026-10-05 | vérifié | **Oui** : « l'État, les autorités régionales ou locales, les organismes de droit public […] ou les associations formées par une ou plusieurs de ces autorités ». Transposée en droit français par la loi de 2005 (lot 1). |
| Directive (UE) 2016/2102, déclaration sur l'accessibilité | Impose aux organismes du secteur public une déclaration sur l'accessibilité de leurs sites et applications. | — | voir registre vérifié | 2026-10-05 | vérifié (considérant 44 et articles correspondants repérés) | Oui, même fondement. Le régime opposable est le droit français de transposition (lot 1). |
| Règlement (UE) 2023/2854 (Data Act), art. 2, point 30 | Définit le « client » d'un fournisseur de services de traitement de données. | — | voir registre vérifié | 2026-10-05 | vérifié | **Oui** : « une personne physique ou morale qui a noué une relation contractuelle avec un fournisseur » ; aucune exclusion des personnes publiques dans la définition lue. |
| Règlement (UE) 2023/2854, art. 29 | Organise la suppression progressive des frais de changement de fournisseur (cloud). | Plus aucun frais de changement à compter du 12 janvier 2027 ; frais réduits du 11 janvier 2024 au 12 janvier 2027 | voir registre vérifié | 2026-10-05 | vérifié | **Oui (bénéficiaire)** : protège la collectivité cliente, argument de réversibilité pour `cloud-hebergement` et `contrats-prestataires`. |
| Règlement (UE) 2024/903 (interopérabilité), art. 2, point 6 | Définit l'« organisme du secteur public » par renvoi à la directive (UE) 2019/1024. | ⚠️ dates d'application non relues | voir registre vérifié | 2026-10-05 | vérifié (définition) ; ⚠️ non vérifié (calendrier, contenu de la directive 2019/1024) | **⚠️ non vérifié** : dépend de la définition de la directive 2019/1024, non lue. |
| Règlement (UE) n° 910/2014 (eIDAS), modifié par le règlement (UE) 2024/1183 | Identification électronique et services de confiance ; le modificatif crée notamment des règles pour les organismes du secteur public qui délivrent des attestations électroniques d'attributs. | ⚠️ dates non relues | voir registre vérifié ; voir registre vérifié | 2026-10-05 | vérifié (existence et objet du modificatif) ; ⚠️ non vérifié (obligation et date d'acceptation des portefeuilles par les organismes publics) | ⚠️ non vérifié pour l'acceptation des portefeuilles d'identité numérique. Ne pas en fixer la date. |
| Règlement (UE) 2016/679 (RGPD), art. 32 | Sécurité du traitement. | — | voir registre vérifié | 2026-10-05 | vérifié (existence et intitulé) | **Pointeur de frontière** : régime traité par `dpo-ct`. |
| Règlement (UE) 2016/679, art. 33 | Notification à l'autorité de contrôle d'une violation de données à caractère personnel. | — | voir registre vérifié | 2026-10-05 | vérifié (existence et intitulé) | **Pointeur de frontière** : régime traité par `dpo-ct`. |

## Points d'attention

1. **Calendrier du règlement IA modifié.** Le règlement (UE) 2026/1744 a
   repoussé l'application des obligations relatives aux systèmes à haut
   risque : 2 décembre 2027 pour l'annexe III, 2 août 2028 pour l'annexe I.
   Pour les systèmes à haut risque des autorités publiques déjà en service,
   l'échéance de mise en conformité est le 2 août 2030. Toute mention du
   calendrier initial (2 août 2026 pour le haut risque) est désormais fausse.
2. **NIS2 et collectivités : double condition.** La directive laisse à
   chaque État membre le choix d'inclure le niveau local, et la France n'a
   pas encore publié sa loi de transposition (lot 2). Le skill ne doit jamais
   dire qu'une collectivité « est soumise à NIS2 ».
3. **Data Act** : fin des frais de changement de fournisseur le 12 janvier
   2027. Cette date est à reporter dans le cache des valeurs.
4. **À compléter dans une passe ultérieure** : calendrier du règlement
   2024/903 et définition de la directive 2019/1024 ; obligations eIDAS des
   organismes publics (acceptation du portefeuille européen d'identité
   numérique) ; liste complète des interdictions de l'art. 5 du règlement IA.
5. **Valeurs à reporter dans le cache daté** : dates de l'art. 113 consolidé
   et de l'échéance 2030 ; 17 et 18 octobre 2024 (NIS2) ; 11 janvier 2024 et
   12 janvier 2027 (Data Act).
