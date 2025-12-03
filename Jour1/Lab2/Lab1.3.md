## 🚀 — Version améliorée du pipeline**

Voici les améliorations que l’on peut enseigner juste après :

---

### 🔥 Amélioration A — Ajouter un tri des clients

Étape : **Sort Rows**

- Trier par `country` puis par `name`
- Placer après `Filter Rows`

---

### 🔥 Amélioration B — Ajouter un champ calculé

Exemple : créer une colonne `email_domain`

Étape : **Formula** ou **User Defined Java Expression**

Expression :

```java
email.substring(email.indexOf("@") + 1)
Résultat :
example.com, dupont.fr, etc.

### 🔥 Amélioration C — Ajouter une gestion des erreurs
Ajouter une sortie "NOK" depuis Filter Rows :

Relier la sortie "False" à un Text File Output

Fichier :
data/customers_errors.csv

- On obtient un pipeline avec flux principal + flux d’erreurs.

---
### 🔥 Amélioration D — Ajouter un enregistrement de logs
Utiliser l’étape : Write to log

Placer après le filtrage

Message :

```bash
${NR_LINES_READ} lignes lues, ${NR_LINES_WRITTEN} lignes écrites.
```
---

### 🔥 Amélioration E — Enrichissement externe
Ajouter un champ continent selon le pays :

Créer un fichier country_to_continent.csv

Utiliser Stream Lookup pour enrichir les données

Exemple :

```csv
Copier le code
country,continent
USA,America
France,Europe
UK,Europe
```

### 🔥 Amélioration F — Pipeline final proposé
```css

CSV Input
    ↓
Filter Rows → Error Output (CSV)
    ↓
Sort Rows
    ↓
Formula (email_domain)
    ↓
Stream Lookup (continent)
    ↓
CSV Output (final_clean_customers.csv)
```
