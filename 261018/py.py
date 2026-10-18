logs = [
    "INFO server started",
    "ERROR database failed",
    "INFO request received",
    "WARNING disk space low",
]

def count_log_levels(logs):
  result = {}
  for log in logs:
    head = log.split(" ")[0]
    if(head in result):
      result[head] += 1
    else:
      result[head] = 1
  return result

print(count_log_levels(logs))
# {"INFO": 2, "ERROR": 1, "WARNING": 1}

def find_problem_logs(logs):
  result = []
  problem = ["ERROR", "WARNING"]
  for log in logs:
    parts = log.split()
    if(parts[0] in problem):
      message = " ".join(parts[1:])
      result.append(message)
  return result

print(find_problem_logs(logs))
# ['database failed', 'disk space low']

def tuple_problem_logs(logs):
  # result = ()
  result = []
  problem = ["ERROR", "WARNING"]

  for log in logs:
    parts = log.split()
    head = parts[0]
    if(head in problem):
      # message = head + ", " + " ".join(parts[1:])
      # result += (message,)
      message = " ".join(parts[1:])
      result.append((head,message))

  return result

print(tuple_problem_logs(logs))
# [('ERROR', 'database failed'), ('WARNING', 'disk space low')]