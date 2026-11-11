from pathlib import Path

def sum_of_category(file_name):
  base_path = Path(__file__).resolve().parent
  answer = {}
  with open(base_path / file_name) as f:
    for line in f:
      k_v = line.split(",")
      try: answer[k_v[0]] += int(k_v[1])
      except KeyError:
        try: answer[k_v[0]] = int(k_v[1])
        except ValueError: continue # まわりくどくなった
  return answer

print(sum_of_category("expenses.csv"))

from csv import DictReader
def dict_reader(file_name):
  base_path = Path(__file__).resolve().parent
  answer = {}
  with open(base_path / file_name) as f:
    reader = DictReader(f)
    for row in reader:
      # try: answer[row["category"]] += int(row["amount"])
      # except KeyError: answer[row["category"]] = int(row["amount"])
      answer[row["category"]] = answer.get(row["category"], 0) + int(row["amount"])
  return answer

print(dict_reader("expenses.csv"))