from pathlib import Path
import os
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
EMPLOYEE_PATH = BASE_DIR / "input/emp.csv"
HOBBIE_PATH = BASE_DIR / "input/hob.csv"
OUTPUT_PATH = BASE_DIR / "output"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

emp = pd.read_csv(EMPLOYEE_PATH)
hob = pd.read_csv(HOBBIE_PATH)

result = pd.merge(emp, hob, "left", "취미이름")
print(result)


output_file = OUTPUT_PATH / "left_joined.csv"
result.to_csv(output_file, index=False)