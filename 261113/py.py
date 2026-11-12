from pathlib import Path
from csv import DictReader

def categorize(file_name):
  base_path = Path(__file__).resolve().parent
  categorized = {}
  invalid_products = []
  with open(base_path / file_name) as f:
    reader = DictReader(f)
    for row in reader:
      try: categorized[row["product"]] = categorized.get(row["product"], 0) + int(row["quantity"])
      except ValueError: invalid_products.append(row["product"])
  return (categorized, invalid_products)

print(categorize("goods.csv"))