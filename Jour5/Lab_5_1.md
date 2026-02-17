# LAB 5.1 — Pipeline SQL → MongoDB

## 🎯 Objectif

Construire un pipeline Apache Hop qui :

- Lit des données depuis une base SQL (PostgreSQL / MySQL)
- Transforme les données
- Écrit les résultats dans MongoDB

---

## 🧠 Contexte 

Relationnel :
- Tables
- Schéma fixe
- Clés étrangères

Document :
- JSON
- Structure flexible
- Données imbriquées

On va passer de :

Table trips


à

{
driver_id: "...",
total_amount: ...,
zone: "...",
...
}


---

## 🔧 Partie 1 — Préparation

### 1️⃣ Base SQL

Créer une table exemple :

```sql
CREATE TABLE taxi_trips (
    id SERIAL PRIMARY KEY,
    vendor_id INT,
    pickup_zone INT,
    dropoff_zone INT,
    trip_distance FLOAT,
    total_amount FLOAT,
    trip_date TIMESTAMP
);
```
Insérer quelques données.

### 2️⃣ MongoDB
Base : taxiDB
Collection : trips

---

#  🚀 Partie 2 — Pipeline Apache Hop
Étapes du pipeline

1. Table Input

2. Select Values

3. MongoDB Output

### 🔹 Étape 1 — Table Input
Requête :
```sql
SELECT 
    id,
    vendor_id,
    pickup_zone,
    dropoff_zone,
    trip_distance,
    total_amount,
    trip_date
FROM taxi_trips;
```

### 🔹 Étape 2 — Select Values
Renommer :

- vendor_id → vendorId

- pickup_zone → pickupZone

- dropoff_zone → dropoffZone

* Pourquoi ?
 Mongo préfère camelCase


### 🔹 Étape 3 — MongoDB Output
Configuration :

Database: taxiDB

Collection: trips

Write concern: ACKNOWLEDGED

Mapping :
```
SQL field → Document field
```

# 🧪 Test
Vérifier dans MongoDB :
```js
db.trips.find().limit(5)
```
---

# 🧠 Questions réflexion
- Quelle différence entre INSERT SQL et Mongo insert ?

- Pourquoi Mongo ne nécessite pas de schéma fixe ?

- Qu’arrive-t-il si un champ est absent ?



