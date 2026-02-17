import pandas as pd

df = pd.read_parquet("yellow_tripdata_2024-01.parquet", engine="pyarrow")

df_small = df.head(10000)

df_small.to_csv("yellow_tripdata_2024_20k.csv", index=False)
