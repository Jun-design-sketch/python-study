import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent
IMPORT_PATH = BASE / "input/expenses.csv"
data = pd.read_csv(IMPORT_PATH)
print(data)

# カテゴリごとの総額を計算し、総額が大きい順で出力する
data_sum = data.groupby(["category"]).sum().drop(columns=['date'])
print(data_sum)

# 日付ごとの支出額を集計し、日付DESCで整列する
data_per_date= data.groupby(["date"])["amount"].sum().sort_index(ascending=False)
print(data_per_date)

# CATEGORYごとの平均支出額を求める
amount_per_category = (
  data.groupby(["category"])["amount"]
  .mean()
  .sort_values(ascending=False)
  .round(0)
  .astype(int)
)
print(amount_per_category)