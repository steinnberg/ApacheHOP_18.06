# 1️⃣ Comment faire le Select Values dans Apache Hop

* Dans le pipeline LAB 5.1 :

```
Table Input → Select Values → MongoDB Output
```

## 🎯 Étape concrète

### 1️⃣ Ajouter un step

Dans Hop :
```
Transform → Select / Rename values
```

Glissez-le entre :

>Table Input → Select Values

2️⃣ Ouvrez le step

Il as plusieurs onglets :

- Select & Alter

- Remove

- Meta-data

- Rename

### Aller dans Rename

3️⃣ Ajouter les renommages

Ajoute :

Field name (original)	Rename to
vendor_id ->	vendorId
pickup_zone	-> pickupZone
dropoff_zone ->	dropoffZone

Puis OK.

### 🔍 Pourquoi utiliser Select Values ?

Ce step permet :

- Renommer

- Supprimer colonnes inutiles

- Changer type (int → string)

- Réordonner

---

## 2️⃣ Où faire MongoDB ?

### MongoDB Atlas (Free tier) est idéal .

1. Pourquoi Atlas ?

    * Gratuit (M0 cluster)

    * Accessible depuis Hop

    * Pas d’installation locale

    * Stable en formation

    * 🚀 Mise en place rapide

---

### Étape de mise en place

1️⃣ Créer compte :
https://www.mongodb.com/atlas

2️⃣ Créer cluster gratuit M0

3️⃣ Database Access → créer user

4️⃣ Network Access → autoriser ton IP

5️⃣ Connect → Copy connection string

---

## 🔌 Connexion dans Apache Hop

Dans Hop :
```
Metadata → MongoDB Connections
```

- Créer nouvelle connexion :

    - Host

    - Username

    - Password

    - Database

    - Test connection.

