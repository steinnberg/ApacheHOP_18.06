import pandas as pd

# 🔹 Lire seulement 5000 lignes
df = pd.read_csv(r"D:\ApacheHOP_18.06\Jour5\taxi_trips.csv", nrows=5000)

# 🔹 Sauvegarder
df.to_csv("taxi_trips_5k.csv", index=False)

print("Extraction terminée : taxi_trips_5k.csv créé")
