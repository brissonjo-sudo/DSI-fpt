# Correction du lanceur de connexion isolée

Le 8 octobre 2026, le lancement de `ouvrir-smoke-dev6.ps1 -Login` échoue
avec « Le fichier spécifié est introuvable ». Le script existe, mais le
chemin fixé de `codex.exe` pointe vers le dossier disparu `8aaf1547b825b104`.

Le lanceur corrigé recherche une application `codex.exe` dans PATH, puis dans
les sous-dossiers du répertoire local `OpenAI/Codex/bin` si nécessaire.
Il refuse explicitement le lancement si aucun exécutable n'est trouvé.
Le profil isolé et le filtrage des variables d'environnement sont conservés.

Le binaire observé est `9691020b546a15b2/codex.exe`, version
`0.162.0-alpha.2`. Trois contrôles réels de `login status` réussissent à
démarrer : PowerShell actuel, Windows PowerShell et PATH sans Codex.
Ils indiquent tous `Not logged in`. La connexion interactive et l'inférence
n'ont pas été exécutées par ces contrôles.

La copie ci-jointe est documentaire : le script s'exécute depuis la racine du
workspace qui contient l'installation isolée. Commande utilisateur :

```powershell
& 'C:\Users\Krn\Documents\Codex\2026-10-06\reprends-le-travail-de-cette-session\ouvrir-smoke-dev6.ps1' -Login
```

L'original reste conservé en octets dans les preuves du 7 octobre et dans
`ouvrir-smoke-dev6-historique-20261007.ps1` à la racine du workspace.
Ce changement de binaire CLI devra être déclaré dans les futures mesures ;
aucun score antérieur n'est transféré et aucun smoke d'usage n'est attesté.
