from collections import Counter

def tokenizer(text):
  tokens = []
  for element in text:
    if not element.isspace():
      tokens.append(element)
  return tokens

"""
  文字列をtokenizeし、2文字毎の登場確率を返却する
"""
def training_bigram(text):
  tokenized = tokenizer(text)
  bi_tokens = {}
  for i in range(len(tokenized)-1):
    key = tokenized[i] + tokenized[i+1]
    if not key in bi_tokens:
      bi_tokens[key] = 1
    else:
      bi_tokens[key] += 1

  total = sum(bi_tokens.values())

  for key, count in bi_tokens.items():
    bi_tokens[key] = count / total

  return bi_tokens

text = "プログラム。。プロ。。ぐ、ら、む"
print(training_bigram(text))