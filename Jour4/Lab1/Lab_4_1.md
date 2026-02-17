# LAB 4.1 — Prise en main de Cypher (Neo4j Cloud)

## 🎯 Objectif pédagogique

Découvrir Cypher, le langage déclaratif de Neo4j.

À la fin du lab, vous saurez :

- Créer des nœuds (CREATE)
- Relier des nœuds (CREATE relationships)
- Utiliser MATCH
- Comprendre MERGE
- Interroger un graphe
- Penser en pattern

---

# 🌐 Étape 0 — Accès à Neo4j en ligne (sans installation)

## Option recommandée : Neo4j Aura Free

1. Aller sur :
   https://neo4j.com/cloud/aura-free/

2. Créer un compte gratuit
3. Créer une base
4. Cliquer sur "Open in Browser"

Vous êtes maintenant dans le Neo4j Browser.

---

# 🧠 Rappel conceptuel

Un graphe contient :

- Nodes (nœuds)
- Relationships (relations)
- Properties (propriétés)

Un nœud peut avoir :
- un label
- des propriétés

Exemple :
(:Driver {name: "Alice"})

---

# 🧪 Étape 1 — CREATE : créer des nœuds

Dans Neo4j Browser, exécutez :

```cypher
CREATE (:Driver {name: "Alice", rating: 4.8})
CREATE (:Driver {name: "Bob", rating: 4.5})
CREATE (:Zone {name: "Manhattan"})
```

Observer :

Apparition des nœuds

Labels différents

# 🧪 Étape 2 — MATCH : rechercher des nœuds
```cypher
MATCH (d:Driver)
RETURN d
```

Question :
Pourquoi utilisons-nous d:Driver ?

# 🧪 Étape 3 — CREATE relation
Créer une relation entre Alice et Manhattan :
```cypher
MATCH (d:Driver {name: "Alice"})
MATCH (z:Zone {name: "Manhattan"})
CREATE (d)-[:DRIVES_IN]->(z)
```
Observer le graphe.

# 🧪 Étape 4 — MATCH avec pattern
```cypher
MATCH (d:Driver)-[:DRIVES_IN]->(z:Zone)
RETURN d.name, z.name
```
Comprendre :
- Cypher est un langage basé sur des patterns graphiques.

# 🧪 Étape 5 — MERGE (clé conceptuelle)
⚠️ CREATE crée toujours un nouvel objet.

MERGE évite les doublons.

Essayez :
```cypher
MERGE (:Driver {name: "Alice"})
```

Puis :
```
MATCH (d:Driver)
RETURN d
```

Question :
Pourquoi MERGE est plus sûr en ETL ?

# 🧪 Étape 6 — WHERE
```cypher
MATCH (d:Driver)
WHERE d.rating > 4.6
RETURN d
```

Comprendre :
Cypher combine logique relationnelle + pattern graph.

# 🧪 Étape 7 — DELETE (optionnel)
```cypher
MATCH (d:Driver {name: "Bob"})
DELETE d
```


#  Étape 8 Supprimer tout le graphe

⚠️ Attention
```cypher
MATCH (n)
DETACH DELETE n
```

# Étape 9 À la fin du lab

Vous devez savoir :

- Créer un graphe simple

- Relier des entités

- Interroger avec MATCH

- Comprendre MERGE

- Lire une requête Cypher


#  Étape 10  Pourquoi ce lab est stratégique

- 100% cloud
- Aucun problème d’installation
- Compréhension conceptuelle 

---
