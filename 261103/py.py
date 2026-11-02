expenses = [
    ("food", 1200),
    ("book", 2500),
    ("food", 800),
    ("transport", 500),
    ("book", 1000),
]

def sum_by_category(expenses):
  result = {}
  for key, value in expenses:
    result[key] = result.get(key, 0) + value
  return result
print(sum_by_category(expenses))

def count_each_category(expenses):
  result = {}
  for expense in expenses:
  # for category, _ in expenses:
    result[expense[0]] = result.get(expense[0], 0) + 1
  return result
print(count_each_category(expenses))