numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
# [1, 4, 9, 16, 25]
print(squares)

# squaresは？
# number*number。は？
# numberから作る。は？
# numbersから順次引き出す。

# squares = []
# for number in numbers:
#   squares.append(number * number)

diction = {'a':2, 'b':3, 'c':4}
dictionaryComprehension = {
  k: v*10
  for k, v in diction.items()
}
print(dictionaryComprehension)