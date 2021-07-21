import pandas as pd

filepath = "data/exoTrain.csv"

df = pd.read_csv(filepath)

schema = []

for column in df.columns:
    info = {"mlcoreType": "number", "type": "float"}
    info["name"] = column
    schema.append(info)

print(schema)
