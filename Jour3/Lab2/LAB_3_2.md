# LAB 3.2 — Data Quality Dashboard

## 🎯 Objectif pédagogique

Créer un mini "Data Quality Dashboard" à partir des métriques du pipeline précédent.

Vous allez :

- Calculer des statistiques de qualité
- Exporter des métriques
- Visualiser l’impact du nettoyage

---

# 🧠 Contexte

Une équipe métier veut savoir :

- Combien de lignes sont rejetées ?
- Quel pourcentage est invalide ?
- Quelle est la moyenne des montants après nettoyage ?
- Combien de valeurs nulles ont été détectées ?

Vous devez produire ces indicateurs.

---

# 🧪 Étape 1 — Compter les lignes

Dans un nouveau pipeline :

1. Lire :
   - taxi_clean.csv
   - taxi_rejected.csv

2. Ajouter :
   - Group By → COUNT(*)

Produire :
- total_clean
- total_rejected

---

# 🧪 Étape 2 — Calcul du taux de rejet

Ajouter :
- Calculator

Formule :
rejection_rate = total_rejected / (total_clean + total_rejected)


---

# 🧪 Étape 3 — Statistiques métier

Sur taxi_clean :

Ajouter :
- Group By

Calculer :
- AVG(total_amount)
- MAX(total_amount)
- MIN(total_amount)

---

# 🧪 Étape 4 — Export Dashboard

Exporter les métriques vers :

Option A :
- CSV : data/clean/quality_metrics.csv

Option B :
- Table SQL

---

# 📊 Résultat attendu

Un fichier contenant :

- total_lines
- total_clean
- total_rejected
- rejection_rate
- avg_total_amount

---

# 🧠 Questions de réflexion

1. Si le taux de rejet dépasse 20 %, que faire ?
2. À partir de quel seuil faut-il alerter ?
3. Qui décide des règles de qualité ?

---

# 🎓 Bonus

Ajouter :
- Un seuil d’alerte
- Une colonne status = OK / WARNING / CRITICAL
