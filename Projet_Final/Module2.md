2️⃣ Data Warehouse & Partitionnement
# 📘 Fiche pédagogique — Module 2
## Data Warehouse & Partitionnement

---

## 🎯 Objectifs pédagogiques
À l’issue de ce module, l’étudiant sera capable de :
- Structurer des données analytiques
- Comprendre le modèle en étoile
- Construire un Data Warehouse simple
- Appliquer un partitionnement efficace

---

## 🧠 Apports théoriques

### 1. Pourquoi un Data Warehouse ?
- Optimisé pour l’analyse
- Séparation faits / dimensions
- Requêtes plus rapides
- Meilleure lisibilité métier

---

### 2. Modèle en étoile
- **Table de faits** : mesures (montants, distances)
- **Dimensions** : contexte (temps, zone, fournisseur)

---

### 3. Partitionnement
- Découpage logique des données
- Par date, par zone, par période
- Réduction du volume scanné

---

## 🧪 Cas concret guidé

### Situation
Les analystes veulent répondre rapidement à :
- Quel est le revenu par zone ?
- Par heure ?
- Par vendor ?

---

### Travail à réaliser
1. Créer les dimensions :
   - Date
   - Zone
   - Vendor
2. Construire la table `FactTrips`
3. Partitionner les données (ex : par mois)
4. Calculer des KPIs simples

---

## 🎁 Livrables attendus
- Schéma du Data Warehouse
- Pipelines Hop dimensions + faits
- Tables exploitables

---

## ✅ Critères de réussite
- Modèle cohérent
- Jointures correctes
- Données partitionnées