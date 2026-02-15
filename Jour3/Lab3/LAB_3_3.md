# LAB 3.3 — Logging avancé & Audit

## 🎯 Objectif pédagogique

Comprendre :

- Comment Hop journalise l’exécution
- Comment analyser les logs
- Comment interpréter les erreurs
- Comment produire un audit simple

---

# 🧠 Pourquoi le logging est critique ?

En entreprise :

- Un pipeline peut tourner à 2h du matin
- Personne ne le regarde
- S’il échoue, il faut comprendre pourquoi

Le logging est votre seule trace.

---

# 🧪 Étape 1 — Activer les logs détaillés

Dans Hop :

- Aller dans Run Configuration
- Activer :
  - Detailed logging
  - Debug mode (si nécessaire)

Exécuter le pipeline Taxi robuste.

Observer :
- Temps d’exécution
- Nombre de lignes traitées
- Warnings
- Errors

---

# 🧪 Étape 2 — Analyser les logs

Identifier :

- Transformation la plus lente
- Nombre de lignes lues
- Nombre de lignes rejetées
- Messages d’erreur

Répondre :

1. Où se situe le goulot d’étranglement ?
2. Quelle transformation est critique ?

---

# 🧪 Étape 3 — Audit simplifié

Créer un pipeline "audit_logger" :

Entrée :
- Variables système
- Métriques calculées

Sortie :
- audit_log.csv

Contenu :
- timestamp
- pipeline_name
- rows_processed
- rows_rejected
- execution_time

---

# 🧠 Étape 4 — Simulation d’erreur

Modifier volontairement :
- Le nom d’une colonne
- Le chemin d’un fichier

Observer :
- Type d’erreur
- Log produit
- Où l’erreur apparaît

---

# 🔍 Questions de réflexion

1. Quelle différence entre error et warning ?
2. Comment diagnostiquer un pipeline qui “ne plante pas mais produit peu de données” ?
3. Pourquoi un log clair vaut mieux qu’un commentaire ?

---

# 🎓 Bonus

Créer un log_level paramétrable :

- INFO
- DEBUG
- ERROR

---

# ✅ Validation finale

Vous devez savoir :

- Lire un log Hop
- Identifier une erreur
- Identifier une lenteur
- Expliquer l’origine d’un échec
