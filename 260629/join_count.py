from pathlib import Path
import pandas as pd

BASE_PATH = Path(__file__).resolve().parent
CUSTOMER_PATH = BASE_PATH / "input" / "顧客.csv"
ORDER_PATH = BASE_PATH / "input" / "注文.csv"
ORDER_INFO_PATH = BASE_PATH / "input" /  "注文明細.csv"
FAQ_PATH = BASE_PATH / "input" /  "問い合わせ.csv"

OUTPUT_PATH = BASE_PATH / "output"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
MERGED_1_PATH = OUTPUT_PATH / "キーごとのCOUNT.csv"

customer = pd.read_csv(CUSTOMER_PATH)
order = pd.read_csv(ORDER_PATH)

order_counts = (
  order
  .groupby("顧客ID(注文)")
  .size()
  .reset_index(name = "！注文数！")
)

result = pd.merge(
  customer,
  order_counts,
  left_on = "顧客ID",
  right_on="顧客ID(注文)",
  how="left"
)

result.to_csv(MERGED_1_PATH)