# LAB 3.1 — Pipeline robuste Taxi

## 🎯 Objectif pédagogique

Construire un pipeline Apache Hop robuste pour :

- Ingestion d’un dataset Taxi (CSV)
- Nettoyage des données
- Validation des champs critiques
- Rejet des lignes invalides
- Séparation des flux "clean" et "errors"

À la fin du lab, vous devez comprendre :
- Comment structurer un pipeline industriel
- Comment gérer les erreurs
- Comment rendre un pipeline rejouable

---

# 🧠 Contexte

Nous travaillons sur un extrait du dataset NYC Taxi.

Certaines lignes contiennent :
- valeurs nulles
- dates incohérentes
- montants négatifs
- coordonnées invalides

Votre mission est de construire un pipeline robuste qui :
1. Nettoie
2. Valide
3. Sépare
4. Exporte

---

# 📂 Structure attendue

data/
├── raw/
├── clean/
└── rejected/


---

# 🧪 Étape 1 — Ingestion CSV

1. Créer un nouveau pipeline
2. Ajouter une transformation :
   - CSV File Input
3. Lire le fichier depuis `data/raw/`

Vérifier :
- Encodage
- Séparateur
- Mapping des colonnes

---

# 🧪 Étape 2 — Typage & Normalisation

Ajouter :
- Select Values (pour typer correctement les champs)
- Date format (si nécessaire)
- Number format (si nécessaire)

Vérifier :
- pickup_datetime
- dropoff_datetime
- total_amount
- passenger_count

---

# 🧪 Étape 3 — Règles de validation

Ajouter une transformation :

## Filter Rows

Règles :
- total_amount > 0
- passenger_count > 0
- pickup_datetime NOT NULL
- dropoff_datetime NOT NULL

Séparer :
- Flux valide → clean
- Flux invalide → rejected

---

# 🧪 Étape 4 — Gestion d’erreur

Configurer :
- Error handling sur les transformations critiques
- Capturer les lignes échouées
- Ajouter une colonne "error_reason"

---

# 🧪 Étape 5 — Export

Flux valide :
- CSV Output → `data/clean/taxi_clean.csv`

Flux invalide :
- CSV Output → `data/rejected/taxi_rejected.csv`

---

# 🔍 Questions de réflexion

1. Que se passe-t-il si une colonne change de nom ?
2. Que se passe-t-il si le fichier contient 10 millions de lignes ?
3. Votre pipeline est-il rejouable ?

---

# 🎓 Bonus

Ajouter :
- Une colonne processing_timestamp
- Une colonne batch_id

---

# ✅ Validation finale

Votre pipeline doit :

- Ne jamais planter
- Séparer clean et rejected
- Être clair visuellement
- Être documenté
