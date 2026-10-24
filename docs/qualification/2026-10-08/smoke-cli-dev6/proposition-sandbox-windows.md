# Prochaine étape soumise à autorisation : sandbox Windows isolé

Les quatre sessions authentifiées terminent, mais cinq résultats d'outils
refusent des lectures avant le lancement de PowerShell avec « blocked by policy ».
Le profil isolé utilise lecture seule et `never`, sans backend Windows déclaré.
Un backend non configuré est la cause probable, sans preuve complète pour cette
build alpha. Une demande d'aide `sandbox windows --help` a déclenché un helper
qui a échoué. Aucune initialisation réussie n'est attestée.

L'étape proposée consiste à initialiser le sandbox natif Windows **elevated**
pour le profil isolé authentifié, en gardant la lecture seule, le web désactivé
et le MCP local désactivé. Cette initialisation peut créer les comptes techniques,
permissions de fichiers et règles de pare-feu nécessaires. Elle dépasse le
périmètre des seuls fichiers du plugin ; une autorisation explicite reste requise.

Après autorisation : inspecter les paramètres effectifs, lancer le mécanisme
officiel de configuration, vérifier une lecture synthétique sans modèle,
contrôler les octets du plugin et capturer un nouveau reçu. Un échec reste
conservé et ne justifie aucun bypass, accès complet ou désactivation des règles.
Aucun profil global ni identifiant d'authentification n'est copié.

La campagne suivante utilisera un protocole, des sessions et un gel nouveaux
sur les octets dev.7. Le smoke dev.6 et tous ses refus resteront conservés.
La présentation v8 décrit le bilan actuel, avec release et avis humains ouverts.

Documentation officielle :
[sandbox Windows](https://learn.chatgpt.com/docs/windows/windows-sandbox)
et [configuration asynchrone via App Server](https://learn.chatgpt.com/docs/app-server).
