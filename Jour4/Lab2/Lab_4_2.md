# LAB 4.2 — Apache Hop → Neo4j (Ingestion Graph)

## 🎯 Objectif pédagogique

Connecter Apache Hop à Neo4j (cloud) pour :

- Lire un dataset Taxi
- Créer des Nodes
- Créer des Relationships
- Comprendre MERGE en contexte ETL

---

# 🧠 Contexte

Nous voulons transformer des données relationnelles en graphe.

Dataset Taxi (simplifié) :
- driver_name
- trip_id
- pickup_zone
- amount

Modélisation Graph cible :

(:Driver)
(:Trip)
(:Zone)

Relations :
(Driver)-[:PERFORMED]->(Trip)
(Trip)-[:TO_ZONE]->(Zone)

---

# 🌐 Étape 1 — Préparation Neo4j Aura

1. Créer base Neo4j Aura Free
2. Noter :
   - URI
   - Username
   - Password

---

# ⚙️ Étape 2 — Configuration connexion Neo4j dans Hop

Dans Hop :

1. Metadata → Neo4j Connection
2. Ajouter :
   - Bolt URI
   - User
   - Password

Tester connexion.

---

# 🧪 Étape 3 — Lecture dataset Taxi

Pipeline :

CSV Input → Select Values → Neo4j Output

---

# 🧪 Étape 4 — Création Nodes (via Cypher)

Utiliser transformation Neo4j Cypher.

Requête pour Driver :

```cypher
MERGE (d:Driver {name: $driver_name})
```

Requête pour Zone :
```cypher
MERGE (z:Zone {name: $pickup_zone})
```

Requête pour Trip :
```cypher
MERGE (t:Trip {id: $trip_id})
SET t.amount = $amount
```
---

# 🧪 Étape 5 — Création Relations
```cypher
MATCH (d:Driver {name: $driver_name})
MATCH (t:Trip {id: $trip_id})
MERGE (d)-[:PERFORMED]->(t)
```
```cypher
MATCH (t:Trip {id: $trip_id})
MATCH (z:Zone {name: $pickup_zone})
MERGE (t)-[:TO_ZONE]->(z)
```

# 🧪 Étape 6 Pourquoi MERGE est essentiel ?

En ETL :

- Évite doublons

- Permet pipeline rejouable

- Garantit cohérence


# 🔎 Vérification dans Neo4j Browser
```cypher
MATCH (n)
RETURN n LIMIT 50
```

### ✅ Validation

Votre pipeline doit :

* Être rejouable

* Ne pas créer de doublons

* Alimenter correctement le graphe