# Split strings in a cell into rows

import pandas as pd

df = pd.read_csv(
    "data.csv",
    encoding="euc-kr",
    usecols=[0, 1, 2, 3, 4],
    names=["A", "B", "C", "D", "E"],
    skiprows=1,
).dropna()

new_df = pd.DataFrame(
    df.E.str.split(",").tolist(), index=[df.A, df.B, df.C, df.D]
).stack()
new_df = new_df.reset_index(["A", "B", "C", "D"])
new_df.columns = ["광고그룹명", "판매자 ID", "사이트", "상품 번호", "키워드"]

# new_df.to_excel("final.xlsx", index=False)
new_df.to_csv("final.csv", index=False, encoding="euc-kr")
