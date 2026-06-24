# python3 -m venv .venv
# source .venv/bin/activate
# pip install pandas openpyxl

import pandas as pd

def classify(argument):
  if argument == "Running":
    return "관련없음", 0
  if argument == "Cooking":
    return "관련있음", 1
  if argument == "Coding":
    return "관련많음", 3
  return "알수없음", -1

def main():
  csv1_path = "input/csv1_employees.csv"
  csv2_path = "input/csv2_hobbies.csv"

  # 読み込む
  employees_data = pd.read_csv(csv1_path)
  hobbies_data = pd.read_csv(csv2_path)

  # DataFrameにない列名を指定し、値を入れると、自動で新たな列ができる
  # pandas.Series()で展開可能であることを示せる
  employees_data[["관련성","관련도"]] = employees_data["취미이름"].apply(
    lambda hobby : pd.Series(classify(hobby))
  )

  print("=== # 列を選択し、条件フィルター ===")
  filtered_data = employees_data[
    employees_data["특기이름"] == "Coding"
  ]
  print(filtered_data)
  

  print("=== 趣味データの確認 ===")
  print(hobbies_data.head())

  print("=== マージ ===")
  # 名前が違ってもleft_on / right_onでマッピング可能
  merged_data = employees_data.merge(
    hobbies_data,
    on="취미이름",
    how="left"
  )
  print(merged_data.head)


main()