import csv
import random

drivers = ["Alice", "Bob", "Carlos", "Diana", "Ethan", "Fatima", "George", "Hana", "Ivan", "Julia"]
zones = ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]

rows = 5000

with open("taxi_small_5k.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["driver_name", "trip_id", "pickup_zone", "amount"])

    for i in range(1, rows + 1):
        driver = random.choice(drivers)
        zone = random.choice(zones)
        amount = round(random.uniform(8, 75), 2)
        trip_id = f"T{i:05d}"

        writer.writerow([driver, trip_id, zone, amount])

print("taxi_small_5k.csv generated successfully.")
