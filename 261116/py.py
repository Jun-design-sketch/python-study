from pathlib import Path

def find_json():
  json_names = []
  base_path = Path(__file__).parent
  # for path in Path.glob(base_path, "*.json"):
  for path in base_path.glob("*.json"):
    json_names.append(path.name)
  json_names.sort()
  return json_names

print(find_json())