import csv
import random
import uuid
from datetime import datetime, timedelta

# Zones organisées par "importance"
central_zones = ["Midtown", "Downtown", "Upper East Side", "Upper West Side"]
mid_zones = ["Brooklyn Heights", "Williamsburg", "Astoria"]
outer_zones = ["Bronx North", "Queens East", "Staten Island"]

all_zones = central_zones + mid_zones + outer_zones

# Drivers (certains très actifs)
high_activity_drivers = ["D001", "D002", "D003"]
medium_activity_drivers = ["D010", "D011", "D012", "D013"]
low_activity_drivers = ["D020", "D021", "D022", "D023", "D024"]

drivers = high_activity_drivers + medium_activity_drivers + low_activity_drivers

start_date = datetime(2024, 1, 1)

def weighted_zone():
    r = random.random()
    if r < 0.5:
        return random.choice(central_zones)
    elif r < 0.8:
        return random.choice(mid_zones)
    else:
        return random.choice(outer_zones)

rows = 5000

with open("taxi_nyc_realistic_5k.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "trip_id",
        "driver_id",
        "pickup_zone",
        "dropoff_zone",
        "amount",
        "trip_date"
    ])

    for i in range(rows):
        trip_id = f"T{i:06d}"

        # Driver pondéré (certains plus actifs)
        r = random.random()
        if r < 0.5:
            driver = random.choice(high_activity_drivers)
        elif r < 0.8:
            driver = random.choice(medium_activity_drivers)
        else:
            driver = random.choice(low_activity_drivers)

        pickup = weighted_zone()
        dropoff = weighted_zone()

        amount = round(random.uniform(10, 90), 2)
        date = start_date + timedelta(minutes=random.randint(0, 60*24*90))

        writer.writerow([
            trip_id,
            driver,
            pickup,
            dropoff,
            amount,
            date.strftime("%Y-%m-%d %H:%M:%S")
        ])

print("taxi_nyc_realistic_5k.csv generated successfully.")
