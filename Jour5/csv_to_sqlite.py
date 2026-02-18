import pandas as pd
from sqlalchemy import create_engine

# 🔹 Charger CSV (prends 20k max si gros fichier)
df = pd.read_csv(r"D:\ApacheHOP_18.06\Jour5\taxi_trips.csv", nrows=20000)

# 🔹 Renommer colonnes pour SQL propre
df = df.rename(columns={
    "VendorID": "vendor_id",
    "PULocationID": "pickup_zone",
    "DOLocationID": "dropoff_zone",
    "trip_distance": "trip_distance",
    "total_amount": "total_amount",
    "tpep_pickup_datetime": "pickup_datetime"
})

# 🔹 Garder seulement colonnes utiles
df = df[[
    "vendor_id",
    "pickup_zone",
    "dropoff_zone",
    "trip_distance",
    "total_amount",
    "pickup_datetime"
]]

# 🔹 Créer base SQLite locale
engine = create_engine("sqlite:///taxi.db")

# 🔹 Écrire table SQL
df.to_sql("taxi_trips", engine, if_exists="replace", index=False)

print("Table taxi_trips créée dans taxi.db")
