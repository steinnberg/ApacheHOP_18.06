# 📘 Fiche pédagogique — Module 1
## Découverte du dataset & Pipeline ETL (Local)

---

## 🎯 Objectifs pédagogiques
À l’issue de ce module, l’étudiant sera capable de :
- Analyser un dataset réel et volumineux
- Identifier des problèmes de qualité de données
- Construire un pipeline ETL local avec Apache Hop
- Appliquer des règles de nettoyage simples et justifiées

---

## 🧠 Apports théoriques

### 1. Qu’est-ce qu’un ETL ?
- **Extract** : lecture de données brutes
- **Transform** : nettoyage, typage, filtrage
- **Load** : stockage dans un format exploitable

👉 En pratique, 80 % du travail d’un Data Engineer concerne la **qualité des données**.

---

### 2. Problèmes classiques dans les données réelles
- Valeurs manquantes
- Valeurs aberrantes (0, négatives, extrêmes)
- Mauvais types (dates en texte, nombres en chaînes)
- Incohérences métier

---

### 3. Dataset NYC Taxi
Exemples de champs critiques :
- `trip_distance` : ne peut pas être négative
- `fare_amount` : ne peut pas être négatif
- `pickup_datetime < dropoff_datetime`
- `total_amount ≈ somme des composantes`

---

## 🧪 Cas concret guidé

### Situation
Vous recevez un fichier CSV de trajets de taxi (plusieurs millions de lignes).  
Votre mission est de **produire un fichier propre et exploitable**.

---

### Travail à réaliser
1. Charger un échantillon du dataset (1 jour ou 1 mois)
2. Supprimer :
   - trajets avec distance ≤ 0
   - montants incohérents
   - dates invalides
3. Convertir les types :
   - dates → timestamp
   - montants → numérique
4. Exporter les données nettoyées

---

## 🎁 Livrables attendus
- Pipeline Apache Hop fonctionnel
- Fichier de données nettoyées
- Justification écrite des règles de nettoyage

---

## ✅ Critères de réussite
- Pipeline exécutable sans erreur
- Données propres et cohérentes
- Règles explicites et compréhensibles
