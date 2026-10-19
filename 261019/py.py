text = "apple banana apple orange banana apple"

def most_written(text):
  dic = {}
  for el in text.split(" "):
    if el in dic:
      dic[el] += 1
    else:
      dic[el] = 1
  return max(dic, key=dic.get)

print(most_written(text))