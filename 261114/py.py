from pathlib import Path
import json

def validate(file_name):
  invalid_ids = []
  quantities = 0

  base_path = Path(__file__).resolve().parent
  with open(base_path / file_name) as f:
    reader = json.load(f)
    for line in reader:
      try: quantity = int(line["quantity"])
      except (ValueError,TypeError): invalid_ids.append(line["id"])
      else:
        if quantity <= 0: invalid_ids.append(line["id"])
        else: quantities += quantity
  return (quantities, invalid_ids)

print(validate("orders.json"))