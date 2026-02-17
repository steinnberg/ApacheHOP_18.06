# LAB 5.2 — Enrichissement Documents MongoDB

## 🎯 Objectif

Transformer les documents pour :

- Ajouter des champs calculés
- Imbriquer des données
- Créer une structure plus analytique

---

## 🧠 Contexte

En SQL :
JOIN + calcul

En Mongo :
Transformation document

---

## 🔧 Étape 1 — Ajouter champ revenue_category

Dans Hop :

Ajouter un step :

🔹 Calculator

Règle :

if total_amount > 50 → "HIGH"
else → "STANDARD"


Champ : revenueCategory

---

## 🔧 Étape 2 — Créer structure imbriquée

Transformer :

Avant :

```json
{
  vendorId: 1,
  pickupZone: 41,
  dropoffZone: 42,
  total_amount: 12.3
}
```
Après :
```json
{
  vendorId: 1,
  route: {
      from: 41,
      to: 42
  },
  financial: {
      total: 12.3,
      category: "STANDARD"
  }
}
```

### Dans Hop
Utiliser :

JSON Output

MongoDB Output (Update mode)

## 🧪 Vérification Mongo
```js
db.trips.find({ "financial.category": "HIGH" })
```

## 🧠 Questions réflexion

- Pourquoi l’imbrication est puissante en NoSQL ?

- Dans quel cas c’est dangereux ?

- Quelle différence avec une jointure SQL ?