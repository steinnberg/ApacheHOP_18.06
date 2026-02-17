import pandas as pd

input_file = r"D:\ApacheHOP_18.06\Jour4\Lab3\taxi_data.csv"
output_file = "taxi_graph_sample_20000.csv"

chunksize = 50000
rows_to_keep = 20000
rows_written = 0

for chunk in pd.read_csv(input_file, chunksize=chunksize):
    
    # garder seulement colonnes utiles
    chunk = chunk[[
        "VendorID",
        "PULocationID",
        "DOLocationID",
        "trip_distance",
        "total_amount"
    ]]
    
    if rows_written == 0:
        chunk.head(rows_to_keep).to_csv(output_file, index=False, mode='w')
    else:
        break
    
    rows_written += len(chunk)

print("Sample file generated successfully.")
