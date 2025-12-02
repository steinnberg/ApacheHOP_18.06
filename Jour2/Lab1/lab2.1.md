
## 🧪 LAB 1 – Extraction multi-source (CSV + MySQL)

### Lab 1 – Multi-source pipeline
    - Source 1 : CSV clients
    - Source 2 : MySQL “orders”
    - Fusion par clé client → fichier unique

---
### 🎯 Objectif

**Créer un pipeline qui :**

- Extrait un fichier CSV contenant les clients
- Extrait une base SQL contenant les commandes
- Fait une jointure par customer_id
- Sort un fichier fusionné customers_orders.csv

---
#### 🧰 Préparation
1️⃣ CSV d’entrée
Placer dans data/customers.csv :
```csv
id,name,country
1,John Doe,USA
2,Jane Doe,France
3,Mark Spencer,UK
```

2️⃣ Table MySQL

Créer une base hop_training :
```
CREATE TABLE orders (
  order_id INT,
  customer_id INT,
  amount DECIMAL(10,2),
  created_at DATE
);

INSERT INTO orders VALUES
(1001, 1, 150.25, '2024-03-02'),
(1002, 1, 90.10, '2024-03-05'),
(1003, 3, 210.00, '2024-03-06');
```

---
#### 🧠 Étapes Hop
1. Lire le CSV

- Étape : CSV File Input
- Fichier : data/customers.csv
- Encodage : UTF-8

2. Lire MySQL

Étape : Table Input
Connexion :
Host : localhost
User : root
DB : hop_training

Requête :
```
SELECT * FROM orders;
```

3. Jointure

Étape : Merge Join
Type : INNER
Champs :
customers.id = orders.customer_id

4. Export
Étape : Text File Output
Fichier : data/customers_orders.csv


#### 🎉 Résultat attendu
```
id,name,country,order_id,amount,created_at
1,John Doe,USA,1001,150.25,2024-03-02
1,John Doe,USA,1002,90.10,2024-03-05
3,Mark Spencer,UK,1003,210.00,2024-03-06
```

---
#### 💪 Challenge Bonus

Créer une version filtrée :
uniquement les commandes > 100 €
triées par date
chargées dans MySQL dans une table orders_filtered