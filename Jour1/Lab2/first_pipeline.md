## Jour 1 – Lab 2 : Premier pipeline ETL avec Apache Hop

Fichier : Jour1/Lab2_first_pipeline.md

🎯 Objectif

Créer un pipeline complet :
Extraction depuis un CSV → Transformation (nettoyage) → Chargement dans un autre fichier CSV.

### 🧰 Matériel fourni

Crée un dossier data/ dans ton projet :

C:\Hop\projects\hello_hop\data\


Ajoute un fichier nommé customers.csv :
```csv
id,name,email,country
1,John Doe,john@example.com,USA
2,Jane Doe,jane@example.com,France
3,,anonymous@example.com,Canada
4,Mark Spencer,,UK
5,Lucie Dupont,lucie@dupont.fr,France
```

### 🧠 Étape 1 : Créer un pipeline

Menu → File → New → Pipeline

Enregistre sous :

C:\Hop\projects\hello_hop\pipelines\clean_customers.hpl

### 🧠 Étape 2 : Extraire les données CSV

Dans la palette à gauche, cherche CSV File Input

Fais-le glisser dans la zone de travail

Double-clique dessus :

File name : data/customers.csv

Header : ✅

Separator : ,

Encoding : UTF-8

Clique sur “Preview” pour voir les lignes.

### 🧠 Étape 3 : Transformation (filtrage)

Cherche l’étape Filter Rows

Connecte-la à ton “CSV Input”

Condition :

email IS NOT NULL AND name IS NOT NULL


Nom du flux “OK” → sortie valide
Nom du flux “NOK” → erreurs (facultatif)

### 🧠 Étape 4 : Chargement (CSV Output)

Cherche Text File Output
Relie “Filter Rows” → “CSV Output”
Configure :
File name : data/customers_clean.csv
Separator : ,
Header : ✅
Clique sur “Preview rows” pour vérifier.


### 🧠 Étape 5 : Exécution et validation

Clique sur le bouton ▶️ “Run”

Observe la console Hop :
5 lignes lues
3 lignes sorties
2 filtrées

Ouvre customers_clean.csv :
```csv
id,name,email,country
1,John Doe,john@example.com,USA
2,Jane Doe,jane@example.com,France
5,Lucie Dupont,lucie@dupont.fr,France
```
---
#### 📚 À retenir

- Hop utilise un modèle visuel : chaque bloc = étape de transformation
- Les connexions entre blocs = flux de données
- On peut visualiser le flux via “Data preview”
- Sauvegarde toujours le pipeline .hpl dans ton projet