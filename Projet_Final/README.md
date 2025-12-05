# 🚖 ETL + Big Data avec Apache Hop (Distribué)
Programme pédagogique complet basé sur le dataset **NYC Taxi Trips**, conçu pour réaliser:
- l’ETL moderne,
- le Big Data distribué,
- l'orchestration,
- et l’usage d’Apache Hop avec Spark.

---

## 🗂️ Plan Global du Projet final

La Roadmap est divisée en **5 modules**, progressifs et orientés pratique.  

---

# 1️⃣ Module 1 — Découverte du dataset & Pipeline ETL local

### 🎯 Objectifs
- Comprendre la structure du dataset NYC Taxi.
- Prendre en main Apache Hop.
- Construire un premier pipeline ETL local.

### 📌 Contenu
- Présentation des fichiers Yellow Cab / Green Cab.
- Analyse des colonnes : dates, montants, distances, géolocations.
- Téléchargement d’un échantillon (janvier).
- Pipeline Hop :
  - Extraction CSV/Parquet  
  - Nettoyage (valeurs aberrantes, types, normalisation)
  - Chargement vers CSV/Parquet ou DB locale (DuckDB/PostgreSQL)

### 🎁 Livrable
Pipeline Hop complet + données nettoyées.

---

# 2️⃣ Module 2 — Data Warehouse & Partitionnement

### 🎯 Objectifs
- Apprendre les bonnes pratiques de structuration de données.
- Construire un mini Data Warehouse (modèle en étoile).
- Préparer la montée en volume.

### 📌 Contenu
- Partitionnement par mois / année / zone géographique.
- Création des dimensions :
  - DimDate
  - DimZone
  - DimVendor
- Création de la table de faits FactTrips
- ETL Hop :
  - Création des tables dim + fact
  - Jointures
  - KPIs : revenu moyen, distance moyenne, tips, heatmaps

### 🎁 Livrable
Data Warehouse complet (fichiers ou DB) + pipeline Hop.

---

# 3️⃣ Module 3 — Passage au Big Data : Hop + Spark distribué

### 🎯 Objectifs
- Exécuter des pipelines en mode distribué.
- Manipuler plusieurs gigas de données en cluster.
- Intégrer Hop avec Spark.

### 📌 Contenu
- Installation cluster Spark standalone (1 master + 2 workers)
- Configuration Hop pour Spark
- Optimisation mémoire & exécuteurs
- Pipeline Spark distribué :
  - Ingestion de l’année complète
  - Nettoyage distribué
  - Agrégations massives (zones, heures, revenus, tips)
  - Jointures avec dimensions

### 🎁 Livrable
Pipeline Hop distribué fonctionnel (Spark).

---

# 4️⃣ Module 4 — Orchestration & Monitoring (en option)

### 🎯 Objectifs
- Orchestrer un pipeline Big Data de bout en bout.
- Ajouter du monitoring et des logs.
- Automatiser les tâches.

### 📌 Contenu
- Workflow Hop : séquence, dépendances, erreurs
- Exécution conditionnelle
- Monitoring Hop Web
- Logging JSON + visualisation
- Exécution via CLI / scripts Python
- Planification (CRON-like)

### 🎁 Livrable
Workflow complet + monitoring + logs.

---

# 5️⃣ Module 5 — Projet Final : ETL Big Data distribué complet

### 🎯 Objectifs
Créer une architecture Big Data de niveau professionnel.

### 📌 Exigences du projet
1. **Pipeline Spark distribué** :
   - ingestion de l’année complète NYC Taxi
   - nettoyage massif
   - création du Data Warehouse
   - calcul d’indicateurs avancés

2. **Orchestration complète** :
   - workflow Hop
   - logs + alertes
   - versions & documentation

3. **Sorties attendues** :
   - warehouse final (parquet + SQL)
   - dashboard (PowerBI, Grafana, Streamlit, Superset) (en option)
   - rapport technique + diagrammes des pipelines

### 🎁 Livrable
Un mini système ETL Big Data opérationnel.

---

## 📌 Bonus : Idées de sujets de projet
- Anomalies de prix / distances (fraude ou erreurs)
- Heatmap des pickups par heure
- Analyse de performance : 1 worker vs 2 vs 4
- Impact de la météo (en ajoutant NOAA)

---

## 📚 Technologies utilisées
- **Apache Hop**
- **Apache Spark** (standalone, 2–4 workers)
- **DuckDB / PostgreSQL**
- **Docker Compose**
- **Grafana / Superset** (option)
- **Python pour orchestration**

---

## ✨ Auteur & Contact
Cours préparé par **Kheireddin Kadri**, Data Scientist & Enseignant-Chercheur.  
Pour toute question : merci d’ouvrir une *issue* dans ce dépôt.

