# LAB 4.2 bis — Neo4j Aura Only (CSV → Graphe sans HOP)

## 🎯 Objectif pédagogique

Construire un graphe à partir d’un fichier CSV Taxi
en utilisant uniquement Neo4j Aura Free (cloud).

À la fin de ce lab, vous saurez :

- Charger un CSV via LOAD CSV
- Utiliser MERGE pour éviter les doublons
- Créer des Nodes et des Relationships
- Ajouter des contraintes
- Vérifier la cohérence du graphe

---

# 🌐 Étape 0 — Créer une base Neo4j Aura

1. Aller sur : https://neo4j.com/cloud/aura-free/
2. Créer un compte
3. Créer une base gratuite
4. Ouvrir Neo4j Browser

---

# 📂 Étape 1 — Préparer le CSV

Votre fichier taxi_small.csv doit contenir au minimum :

- driver_name
- trip_id
- pickup_zone
- amount

⚠️ Important :
Le fichier doit être accessible publiquement.

Option recommandée :
- Le placer sur GitHub
- Copier l’URL RAW

Exemple :

https://raw.githubusercontent.com/username/repo/main/data/taxi_small.csv


---

# 🧪 Étape 2 — Tester le LOAD CSV

Dans Neo4j Browser :

```cypher
LOAD CSV WITH HEADERS FROM 
"https://raw.githubusercontent.com/username/repo/main/data/taxi_small.csv"
AS row
RETURN row
LIMIT 5;
```
Si des lignes apparaissent → OK ✅

---

# 🧱 Étape 3 — Création des contraintes (IMPORTANT)

Avant ingestion complète :
```cypher
CREATE CONSTRAINT driver_unique IF NOT EXISTS
FOR (d:Driver)
REQUIRE d.name IS UNIQUE;
```
```cypher
CREATE CONSTRAINT trip_unique IF NOT EXISTS
FOR (t:Trip)
REQUIRE t.id IS UNIQUE;
```

---

- Pourquoi ?

- Éviter doublons

- Permettre rejouabilité

- Sécuriser le modèle

---

# 🧪 Étape 4 — Création des Nodes & Relations
```cypher
LOAD CSV WITH HEADERS FROM 
"https://raw.githubusercontent.com/username/repo/main/data/taxi_small.csv"
AS row

MERGE (d:Driver {name: row.driver_name})
MERGE (z:Zone {name: row.pickup_zone})
MERGE (t:Trip {id: row.trip_id})

SET t.amount = toFloat(row.amount)

MERGE (d)-[:PERFORMED]->(t)
MERGE (t)-[:TO_ZONE]->(z);
```

---

# 🔎 Étape 5 — Vérification du graphe
```cypher
MATCH (n)
RETURN n
LIMIT 50;
```

Puis :
```cypher
MATCH (d:Driver)-[:PERFORMED]->(t:Trip)
RETURN d.name, COUNT(t) AS nb_trips
ORDER BY nb_trips DESC;
```
---

# 🔄 Étape 6 — Rejouer la requête

* Relancer l’ingestion.

### Question :

1. Le nombre de nodes augmente-t-il ?

2. Pourquoi ?

---

# 🧠 Étape 7 — Exploration graphe

Trouver :

Les zones les plus fréquentées :
```cypher
MATCH (t:Trip)-[:TO_ZONE]->(z:Zone)
RETURN z.name, COUNT(t) AS trips
ORDER BY trips DESC;
```



Les drivers opérant dans plusieurs zones :
```cypher
MATCH (d:Driver)-[:PERFORMED]->(:Trip)-[:TO_ZONE]->(z:Zone)
RETURN d.name, COUNT(DISTINCT z) AS zones
ORDER BY zones DESC;
```


# 🧠 Questions de réflexion

* Pourquoi MERGE est préférable à CREATE ici ?

* Pourquoi les contraintes sont essentielles en ingestion ?

* Quelle différence avec un import SQL classique ?

* Que se passerait-il sans toFloat(row.amount) ?

* Le graphe permet-il des analyses plus naturelles que SQL ?