# LAB 5.3 — MongoDB Aggregation Framework

## 🎯 Objectif

Utiliser l’Aggregation Pipeline MongoDB pour :

- Grouper
- Compter
- Calculer
- Trier

---

## 🧠 Contexte

SQL :

```sql
SELECT pickup_zone, SUM(total_amount)
FROM taxi_trips
GROUP BY pickup_zone;
```


Mongo :

**Aggregation pipeline**

### 🔧 Exercice 1 — Revenue par zone
```js
db.trips.aggregate([
  {
    $group: {
      _id: "$route.from",
      totalRevenue: { $sum: "$financial.total" },
      tripCount: { $sum: 1 }
    }
  },
  {
    $sort: { totalRevenue: -1 }
  }
])
```

### 🔧 Exercice 2 — Revenue moyen par Vendor
```js
db.trips.aggregate([
  {
    $group: {
      _id: "$vendorId",
      avgRevenue: { $avg: "$financial.total" }
    }
  }
])
```

### 🔧 Exercice 3 — Filtrer HIGH uniquement
```js
db.trips.aggregate([
  { $match: { "financial.category": "HIGH" } },
  {
    $group: {
      _id: "$route.from",
      total: { $sum: "$financial.total" }
    }
  }
])
```