work_hours = {
    "Mina": "8",
    "Jun": "seven",
    "Yuki": "6",
    "Sora": "N/A",
}

def conv(work_hours):
  total_hours = 0
  invalid_names = []
  for key, value in work_hours.items():
    if(str.isnumeric(value)):
      total_hours += int(value)
    else:
      invalid_names.append(key)
  return (total_hours, invalid_names)

print(conv(work_hours))

def tc(work_hours):
  total_hours = 0
  invalid_names = []
  for key, value in work_hours.items():
    try:
      total_hours += int(value)
    except ValueError:
      invalid_names.append(key)
  return (total_hours, invalid_names)

print(tc(work_hours))