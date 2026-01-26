## 🧪 LAB 2 – Extraction depuis une API REST + JSON Parsing


### 🎯 Objectif

1. Créer un pipeline qui :

Appelle une API météo
Récupère un JSON
Parse les données (température, time)
Exporte un CSV

**🌐 API utilisée**

Open-Meteo (api ouverte, pas de clé) :
```bash

https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&hourly=temperature_2m
```

Cela renvoie un JSON.

---

#### 🧠 Étapes Hop
1. **Appeler l’API**

Étape : **HTTP Client**
URL : (mettre dans un champ variable)
```
https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&hourly=temperature_2m
```
Sortie : chaîne JSON

2. **Parser le JSON**
Étape : **JSON Input**
Sélectionner le champ contenant la réponse API
Chemin JSON :
```css
hourly.time[*]
hourly.temperature_2m[*]
```

3. Combiner les colonnes
Étape : **Join Rows on Natural Key**
OU plus simple : Add sequence + merge

4. Export
Étape : **CSV Output**
Fichier :<data/meteo_paris.csv>

#### 🎉 Résultat attendu
```csv
time,temperature_2m
2024-03-02T01:00,6.2
2024-03-02T02:00,5.9
...
```
