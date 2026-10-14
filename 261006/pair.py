def is_valid_parentheses(text):
  l = []
  b = False
  for element in text:
    if element == "(":
      b = True
    l.append(element)
  l.

print(is_valid_parentheses("(a + b) * (c - d)"))
# True
print(is_valid_parentheses("(()"))
# False