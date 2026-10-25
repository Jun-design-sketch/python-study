text = "learn python with small exercises"

def from_long(text):
  arr = text.split()
  # so = sorted(arr, key=lambda item:len(item), reverse=True)
  so = sorted(arr, key=len, reverse=True)
  return so

print(from_long(text))