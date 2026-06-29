from pathlib import Path
import pandas as pd
import numpy as np

BASE_PATH = Path(__file__).resolve().parent
CUSTOMER_PATH = BASE_PATH / "input" / "顧客.csv"
ORDER_PATH = BASE_PATH / "input" / "注文.csv"
ORDER_INFO_PATH = BASE_PATH / "input" /  "注文明細.csv"
FAQ_PATH = BASE_PATH / "input" /  "問い合わせ.csv"

OUTPUT_PATH = BASE_PATH / "output"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
MERGED_1_PATH = OUTPUT_PATH / "異なる列を合計し、MERGE先に表示する.csv"

customer = pd.read_csv(CUSTOMER_PATH)
order = pd.read_csv(ORDER_PATH)

order["純売り上げ"] = order["小計金額"] - order["割引金額"] - order["送料"]
per_customer = order.groupby("顧客ID(注文)", as_index = False).sum()

merged = customer.merge(
  per_customer,
  how = "left",
  left_on = "顧客ID",
  right_on = "顧客ID(注文)"
)

merged.to_csv(MERGED_1_PATH)