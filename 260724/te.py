def most_common_char(word):
  li = list(word)
  dic = dict()

  for element in li:
    if element in dic:
      dic[element] += 1
    else:
      dic[element] = 1

  return max(dic, key=dic.get)

print(most_common_char("banana"))
print(most_common_char("wolfkuncollection"))