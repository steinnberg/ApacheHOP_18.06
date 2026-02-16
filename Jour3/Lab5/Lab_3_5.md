# LAB 3.5 — Stress Test & Résilience Pipeline

## 🎯 Objectif pédagogique

Tester la robustesse d’un pipeline face à :

- données corrompues
- colonnes manquantes
- volumes plus importants
- erreurs système

Comprendre :
- où le pipeline casse
- comment le rendre résilient

---

# 🧠 Contexte

Un pipeline en entreprise doit survivre à :

- fichiers partiellement corrompus
- changements de schéma
- volumes inattendus

Votre mission :
mettre votre pipeline à l’épreuve.

---

# 🧪 Étape 1 — Corruption contrôlée

Modifier volontairement le fichier CSV :

- Supprimer une colonne
- Renommer une colonne
- Introduire des caractères invalides
- Mettre une date invalide

Exécuter le pipeline.

Observer :
- Où l’erreur apparaît ?
- Le pipeline s’arrête-t-il ?
- Les logs sont-ils explicites ?

---

# 🧪 Étape 2 — Gestion proactive

Ajouter :

- Validation de schéma
- Valeurs par défaut
- Error handling
- Logs détaillés

Re-exécuter.

Comparer :
- comportement initial
- comportement amélioré

---

# 🧪 Étape 3 — Simulation de volume

Dupliquer le dataset pour simuler un volume ×5.

Observer :
- temps d’exécution
- transformation la plus lente
- mémoire utilisée (si observable)

---

# 🧠 Questions de réflexion

1. Quelle transformation devient le goulot d’étranglement ?
2. Le pipeline est-il scalable ?
3. Quelle partie dépend le plus de la qualité du schéma ?

---

# 🧪 Étape 4 — Résilience avancée

Ajouter :

- un contrôle préalable du fichier (existence, taille)
- une branche workflow en cas d’échec
- un message d’alerte simulé

---

# 🧠 Analyse professionnelle

Imaginez :

- pipeline exécuté à 2h du matin
- échec silencieux
- reporting faux le matin

Quels mécanismes doivent être en place ?

---

# 🎓 Bonus

Créer un "health check pipeline" :

- vérifie :
    - nombre de colonnes
    - nombre de lignes
    - seuil minimal attendu
- renvoie :
    - OK
    - WARNING
    - CRITICAL

---

# ✅ Validation

À la fin de ce lab, vous devez savoir :

- Identifier une fragilité
- Corriger un point faible
- Anticiper un problème futur

