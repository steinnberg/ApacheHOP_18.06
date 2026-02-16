# LAB 3.4 — Simulation de Dette Data

## 🎯 Objectif pédagogique

Comprendre concrètement ce qu’est la "data debt" (dette data) et comment
un pipeline mal conçu peut produire des effets secondaires invisibles.

Vous allez volontairement créer un pipeline fragile,
observer ses conséquences,
puis le corriger.

---

# 🧠 Contexte

La dette data correspond à :

- règles implicites
- absence de validation
- hypothèses non documentées
- transformations silencieuses

Dans ce lab, vous allez comparer :

1. Un pipeline "rapide mais fragile"
2. Un pipeline robuste et explicite

---

# 🧪 Étape 1 — Pipeline fragile

Créer un pipeline minimal :

CSV Input → Select Values → CSV Output

⚠️ Sans :
- validation
- gestion d’erreur
- contrôle des valeurs

Exécuter.

Observer :
- lignes négatives conservées ?
- nulls présents ?
- incohérences ?

---

# 🧪 Étape 2 — Analyse des conséquences

Créer un second pipeline qui :

- Calcule AVG(total_amount)
- Compte les passagers
- Détecte les montants négatifs

Comparer :
- résultats du pipeline fragile
- résultats d’un pipeline propre

---

# 🧠 Questions

1. Quelle est la différence dans les statistiques finales ?
2. Une moyenne peut-elle masquer un problème ?
3. Pourquoi la dette data est souvent invisible ?

---

# 🧪 Étape 3 — Correction

Modifier le pipeline fragile :

- Ajouter validation
- Ajouter rejet
- Ajouter logging

Comparer à nouveau les métriques.

---

# 🧠 Réflexion professionnelle

Imaginez :

- un modèle ML entraîné sur les données fragiles
- un reporting financier basé sur ces données

Quels impacts ?

---

# 🎓 Bonus

Ajouter :
- un indicateur de qualité global
- une colonne "data_quality_score"

---

# ✅ Validation

Vous devez être capable d’expliquer :

- ce qu’est la dette data
- comment elle se crée
- comment l’éviter

