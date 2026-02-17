# LAB 5.4 — Mongo + Neo4j Hybride (Option Avancé)

## 🎯 Objectif

Comprendre comment combiner :

- MongoDB → stockage document analytique
- Neo4j → analyse relationnelle avancée

But : exploiter les forces complémentaires des deux modèles.

---

# 🧠 Contexte Architecture

**MongoDB :**
- Stockage brut
- Documents enrichis
- Agrégations rapides

**Neo4j :**
- Analyse réseau
- Centralité
- Détection communautés
- Pathfinding

---

# 🎯 Cas d’étude Taxi

MongoDB :
- Stocke les trajets enrichis

Neo4j :
- Analyse les flux entre zones

---

# 🏗️ Architecture cible

MongoDB
    ↓
Export JSON / CSV
    ↓
Apache Hop
    ↓
Neo4j
    ↓
Analyse réseau

---

# 🔧 Partie 1 — Export Mongo vers CSV

Depuis Mongo Shell :

```js
mongoexport \
  --db taxiDB \
  --collection trips \
  --type=csv \
  --fields vendorId,route.from,route.to,financial.total \
  --out mongo_export.csv
  ```
---

# 🔧 Partie 2 — Pipeline Hop Mongo → Neo4j

Pipeline :

MongoDB Input

Select Values

Neo4j Output

MongoDB Input
Requête :
```js
{}
```

Projection :

    - vendorId

    - route.from

    - route.to

    - financial.total

Neo4j Output
Modèle cible :
```ruby
(:Zone)-[:FLOW {amount}]->(:Zone)
```

Cypher logique :
```cypher
MERGE (z1:Zone {id: $from})
MERGE (z2:Zone {id: $to})
MERGE (z1)-[f:FLOW]->(z2)
SET f.total = coalesce(f.total, 0) + $amount
```
---

# 🎯 Partie 3 — Analyse dans Neo4j

Zones les plus influentes
```cypher
MATCH (z:Zone)
RETURN z.id,
       COUNT { (z)-[:FLOW]->() } AS degree
ORDER BY degree DESC;
Flux les plus forts
MATCH (z1:Zone)-[f:FLOW]->(z2:Zone)
RETURN z1.id, z2.id, f.total
ORDER BY f.total DESC
LIMIT 10;
```
---

## 🧠 Discussion

Pourquoi hybride ?

**Mongo :**

Analytics volumique

Documents complexes

**Neo4j :**

Analyse réseau

Structure relationnelle profonde

---

# 🎓 Objectif validé si
- Données Mongo visibles dans Neo4j

- Graphe exploitable

- Centralité calculable

# 🔥 Réflexion avancée
- Dans quel cas une architecture hybride est préférable ?

    * Recommandation

    * Fraud detection

    * Supply chain

    * IoT

