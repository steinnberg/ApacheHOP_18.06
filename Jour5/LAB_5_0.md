# LAB 5 — CSV → MongoDB Atlas (Version Light)

## 🎯 Objectif

- Importer un CSV taxi (50k lignes)
- Le transformer en documents JSON
- L’importer dans MongoDB Atlas
- Manipuler et imbriquer les données

---

# 🧠 Partie 1 — Comprendre le modèle

CSV = données plates :

VendorID,PULocationID,DOLocationID,trip_distance,total_amount,tpep_pickup_datetime

MongoDB = documents JSON flexibles :

{
  vendorId: 1,
  route: {
    from: 41,
    to: 42
  },
  financial: {
    total: 12.3,
    distance: 2.1
  },
  pickupDatetime: ISODate(...)
}

---

# 🚀 Partie 2 — Créer MongoDB Atlas (Free)

1️⃣ Aller sur :
https://www.mongodb.com/atlas

2️⃣ Créer un cluster M0 (gratuit)

3️⃣ Database Access → créer user

4️⃣ Network Access → autoriser ton IP

5️⃣ Ouvrir "Data Explorer"

---

# 📦 Partie 3 — Import CSV directement dans Atlas

## Option simple (sans Python)

1️⃣ Dans Atlas → Data Explorer
2️⃣ Créer Database : taxiDB
3️⃣ Créer Collection : trips
4️⃣ Cliquer sur "Add Data"
5️⃣ Upload CSV
6️⃣ Cocher "First row as header"

⚠️ Mongo va créer un document plat :

{
  VendorID: 1,
  PULocationID: 41,
  DOLocationID: 42,
  trip_distance: 2.3,
  total_amount: 12.4
}

---

# 🧠 Partie 4 — Transformer les documents (imbriquer)

Maintenant on va restructurer les documents.

## Étape 1 — Ajouter champs imbriqués

Dans Mongo Shell (Atlas) :

```js
db.trips.updateMany(
  {},
  [
    {
      $set: {
        vendorId: "$VendorID",
        route: {
          from: "$PULocationID",
          to: "$DOLocationID"
        },
        financial: {
          total: "$total_amount",
          distance: "$trip_distance"
        }
      }
    }
  ]
)
```

## Étape 2 — Supprimer les anciens champs plats
```js
db.trips.updateMany(
  {},
  {
    $unset: {
      VendorID: "",
      PULocationID: "",
      DOLocationID: "",
      total_amount: "",
      trip_distance: ""
    }
  }
)
```
### 🎯 Résultat attendu

Document final :
```
{
vendorId: 1,
route: {
from: 41,
to: 42
},
financial: {
total: 12.4,
distance: 2.3
},
tpep_pickup_datetime: "2024-01-01..."
}
```

---

# 🔎 Partie 5 — Manipulations simples

1️⃣ Trouver trajets > 50$
```js
db.trips.find({ "financial.total": { $gt: 50 } })
```
2️⃣ Compter trajets par zone
```js
db.trips.aggregate([
  {
    $group: {
      _id: "$route.from",
      totalTrips: { $sum: 1 }
    }
  }
])
```

3️⃣ Revenue total
```js
db.trips.aggregate([
  {
    $group: {
      _id: null,
      totalRevenue: { $sum: "$financial.total" }
    }
  }
])
```

