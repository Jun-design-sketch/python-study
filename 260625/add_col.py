from pathlib import Path
import os
import pandas as pd

print(os.getcwd())
BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "input/csv1_employees.csv"

def mapper(key):
  if key == "Cooking":
    return "料理"
  elif key == "Coding":
    return "コーディング"
  else:
    return "その他"

def main():
  contents = pd.read_csv(csv_path)
  # 列が増える
  contents["存在しない列"] = 1

  #増やした列に任意の値をマッピングしてみる
  contents["新たな列"] = contents["특기이름"].apply(
    lambda good_at : mapper(good_at)
  )

  # 複数の列を引数に
  # contents["複数の引数を利用した列"] = contents[["특기이름","취미이름"]].apply(
  #   lambda args : args["특기이름"] == args["취미이름"],
  #   axis = 1
  # )

  # apply()なしでも
  contents["複数の引数を利用した列"] = contents["특기이름"] == contents["취미이름"]

  output_dir = BASE_DIR / "output"
  output_path = output_dir / "csv_modified_1.csv"

  output_dir.mkdir(exist_ok=True)
  contents.to_csv(output_path, index=False, encoding="utf-8-sig")

main()