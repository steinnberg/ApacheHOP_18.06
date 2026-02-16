# LAB 4.3 — Cypher avancé & requêtes analytiques

## 🎯 Objectif pédagogique

Exploiter le graphe pour produire des analyses impossibles ou complexes en SQL.

---

# 🧪 1️⃣ Total revenue par Driver

```cypher
MATCH (d:Driver)-[:PERFORMED]->(t:Trip)
RETURN d.name, SUM(t.amount) AS total_revenue
ORDER BY total_revenue DESC
```

---

🧪 2️⃣ Zone la plus fréquentée
```cypher
MATCH (t:Trip)-[:TO_ZONE]->(z:Zone)
RETURN z.name, COUNT(t) AS trips
ORDER BY trips DESC
```

---

# 🧪  Driver opérant dans plusieurs zones
```cypher
MATCH (d:Driver)-[:PERFORMED]->(:Trip)-[:TO_ZONE]->(z:Zone)
RETURN d.name, COUNT(DISTINCT z) AS zones
ORDER BY zones DESC
```

---

```cypher
# 🧪  Pattern à 2 sauts
MATCH (d:Driver)-[:PERFORMED]->(:Trip)-[:TO_ZONE]->(z:Zone)
RETURN d, z
```

---


# 🧪 Détection d’activité élevée
```cypher
MATCH (d:Driver)-[:PERFORMED]->(t:Trip)
WITH d, COUNT(t) AS nb_trips
WHERE nb_trips > 10
RETURN d.name, nb_trips
```

---
# 🧠 Concepts clés

- Pattern matching

- WITH

- Aggregation

- COUNT DISTINCT

- Multi-hop traversal