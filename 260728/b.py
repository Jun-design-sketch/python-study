from collections import Counter

def tokenizer(text):
  tokens = []
  for element in text:
    if not element.isspace():
      tokens.append(element)
  return tokens

text = "プログラム。。プロ。。ぐ、ら、む"
print(tokenizer(text))