## 🧩 Jour 1 – Lab  : Installation et première exécution d’Apache Hop (mode local)

### Fichier : Jour1/Installation.md

#### 🎯 Objectif

> Installer et lancer Apache Hop en local (sans Docker), vérifier que l’environnement Java est  compatible, puis ouvrir le GUI pour créer son premier projet.

#### 🧰 Prérequis
    - Windows, macOS ou Linux
    - Java JDK 11 ou supérieur
    - 2 Go de RAM minimum
    - Accès Internet pour le téléchargement

---

#### 🧠 Étape 1 : Vérifier Java

Ouvrir un terminal ou PowerShell et tape :

``java -version
``

✅ Résultat attendu :

openjdk version "11.0.18" 2023-01-17
OpenJDK Runtime Environment (build ...)


❌ Si la commande échoue :

Installe AdoptOpenJDK 11 depuis :
👉 https://adoptium.net/temurin/releases/?version=11



#### 🧠 Étape 2 : Télécharger Apache Hop

Rends-toi sur le site officiel :
🔗 https://hop.apache.org/download/

Télécharge :

apache-hop-client-<version>-v2.16.0.zip


Exemple :

apache-hop-client-2.8.0.zip


Décompresse le dossier dans :

C:\Hop\  (Windows)
ou
~/Hop/  (Linux / macOS)


#### 🧠 Étape 3 : Lancer Hop GUI
Sous Windows :

Double-clique sur :

C:\Hop\hop-gui.bat

Sous macOS / Linux :
cd ~/Hop/
sh hop-gui.sh


💡 Si il y a une erreur Java, vérifie la variable d’environnement :

JAVA_HOME = C:\Program Files\Java\jdk-11


#### 🧠 Étape 4 : Créer ton premier projet

Ouvre Hop GUI

Menu → Projects → New Project

Nom : hello_hop

Emplacement : C:\Hop\projects\hello_hop

Clique sur Create and Close

Le projet est maintenant prêt à accueillir tes pipelines et workflows.

#### 🧠 Étape 5 : Vérification

✅ Hop s’ouvre correctement
✅ Un répertoire hello_hop est créé
✅ Aucun message d’erreur Java
✅ Tu peux fermer et rouvrir Hop GUI

#### 📚 À retenir

Apache Hop nécessite Java ≥ 11

Le GUI (hop-gui) est l’interface principale de conception

Chaque projet est un environnement isolé contenant ses pipelines et workflows
