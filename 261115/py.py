from pathlib import Path
import json

result = {
    "total_quantity": 5,
    "invalid_ids": ["A-102", "A-103"],
}

def dump_json(result):
  base_path = Path(__file__).resolve().parent
  with open(base_path / "report.json", "w", encoding="UTF-8") as f:
    json.dump(result, f, indent=4)
  with open(base_path / "report.json", "r", encoding="UTF-8") as f:
    answer = json.dumps(json.load(f), indent=4)
  return answer

print(dump_json(result))