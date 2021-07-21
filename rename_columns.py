import pandas as pd

filepath = "data/exoTrain.csv"

df = pd.read_csv(filepath)

mapping = {}

for column in df.columns:
    if "." in column:
        mapping[column] = column.replace(".", "")
    else:
        mapping[column] = column

df = df.rename(columns=mapping)

df.to_csv(filepath, index=False)
