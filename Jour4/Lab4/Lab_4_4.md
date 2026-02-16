# MINI-PROJET — Graph Taxi Analytics

## 🎯 Objectif

Construire une mini-plateforme graphe Taxi complète :

- Ingestion via Hop
- Analyse via Cypher
- Visualisation via Neo4j Browser

---

# 🧠 Problématique

Un manager veut :

- Top drivers
- Zones les plus actives
- Relations entre zones
- Revenus cumulés

---

# 🧱 Étapes

1. Ingestion Hop
2. Vérification absence doublons
3. Création contraintes (bonus)

```cypher
CREATE CONSTRAINT driver_unique IF NOT EXISTS
FOR (d:Driver)
REQUIRE d.name IS UNIQUE;
```

# Analyse avancée

### 📊 Livrables attendus
* Pipeline Hop

* Requêtes Cypher

* Screenshot graphe

* README explicatif

# 🎓 Bonus avancé
- Créer relation :
```cypher
(:Zone)-[:CONNECTED_TO]->(:Zone)
```
Basée sur trajets successifs.

# ✅ Critères d’évaluation

- Qualité modélisation

- Absence doublons

- Pertinence requêtes

- Clarté README

