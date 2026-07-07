import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent.absolute()
INPUT_PATH = BASE_PATH / "input" / "sales.csv"

data = pd.read_csv(INPUT_PATH)
data["revenue"] = data["quantity"] * data["price"]

sorted_data = (
  data
  .drop("date", axis=1)
  .groupby("product")[["revenue"]]
  .sum()
  .sort_values("revenue", ascending=False)
)
print(sorted_data)

date_sorted_data = (
  data
  .groupby("date")[["revenue","quantity"]]
  .sum()
  .reset_index()
  .sort_values("date", ascending=True)
)
print(date_sorted_data)