from pathlib import Path

def sum_expenses(name):
  b = Path(__file__).resolve().parent
  s = 0
  i = []
  with open(b / name) as f:
    for line in f:
      try: s += int(line)
      except ValueError: i.append(line.strip())
  with open(b / "summary.txt", "w") as w:
    res = f'total: {s}\ninvalid: {", ".join(i)}\ninvalid_count: {len(i)}'
    w.write(res)
  return (s, i)

print(sum_expenses("expenses.txt"))
# 5500