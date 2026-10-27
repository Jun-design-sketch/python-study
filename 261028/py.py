text = "learn python with small exercises every day"

def from_long_words(text):
  arr = text.split()
  more_than_four = []
  for el in arr:
    if len(el) > 4:
      more_than_four.append(el)
  answer = sorted(more_than_four, key=len, reverse=True)
  return answer

print(from_long_words(text))