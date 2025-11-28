## 🧭 Jour 1 — Introduction à l’ETL et à Apache Hop
### 🎯 Objectifs pédagogiques

**Comprendre les concepts ETL et Big Data**

- Découvrir Apache Hop : philosophie, composants, interface
- Installer et configurer Hop en mode standalone
- Créer son premier pipeline : Extraction → Transformation → Chargement
---

### 🧠 Fiche Théorique

1. Concepts ETL

2. Extract : obtenir la donnée brute

3. Transform : nettoyer, enrichir, harmoniser

4. Load : injecter dans une base ou un fichier cible

5. Enjeux : 
    * fiabilité
    * qualité
    * scalabilité
    * performance

---
### Apache Hop

- Composants : Pipelines, Workflows, Actions, Metadata

- Philosophie : modularité, open source, extensibilité

- Installation & Prérequis

- Installer Java 11+ (java --version)

> Télécharger Hop : https://hop.apache.org/download

> Extraire → lancer hop-gui.sh ou hop-gui.bat

> Alternative Docker :
`Bash`
docker run -it -p 8182:8182 apache/hop-web
``

Vérifier la configuration via Hop GUI