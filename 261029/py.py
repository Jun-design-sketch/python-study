text = "python is fun and python is practical"

def remove_duplicated(text):
  arr = text.split()
  new_arr = []
  for el in arr:
    if el not in new_arr:
      new_arr.append(el)
  return new_arr

print(remove_duplicated(text))

# set()で判定しても良い
def remove_duplicated(text):
  seen = set()
  new_arr = []

  for el in text.split():
    if el not in seen:
      seen.add(el)
      new_arr.append(el)
  return new_arr

print(remove_duplicated(text))

'''
---------------------------------------------
'''

expenses = [1200, 3500, 800, 4200, 1500]
limit = 3000

def find_over_limit_and_sum(expenses, limit):
  result = []
  total = 0

  for expense in expenses:
    if expense > limit:
      result.append(expense)
      total += expense
  return result, total # tuple

print(find_over_limit_and_sum(expenses, limit))

'''
---------------------------------------------
'''

