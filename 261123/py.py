tasks = [
    {"title": "monthly report", "days_left": 3},
    {"title": "client reply", "days_left": 1},
    {"title": "backup", "days_left": 7},
]
def has_urgent_task(tasks):
  l = [task for task in tasks if task["days_left"] <= 1]
  print(l)
  return any(l)

print(has_urgent_task(tasks))