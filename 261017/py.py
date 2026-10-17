numbers=[3,8,1,6,7,4]
evens=[]
for element in numbers:
  if element%2 == 0:
    evens.append(element*10)
print(evens)

files=["memo.txt", "photo.jpg", "todo.txt", "music.mp3", "double.dot.txt"]
target=[]
for element in files:
  # if element.split(".")[1] == "txt":
  #   target.append(element)
  if element.endswith(".txt"):
    target.append(element.upper())
print(target)

names=["aaaaa","CCCCCC","xxxxxx","iiiiiiiiiiiii","dd","mmf"]
target=[]
for element in names:
  if len(element) >= 4:
    target.append(element.upper())
print(target)

numbers = [3, 8, 1, 6, 7, 4]
total = 0
for element in numbers:
  if element%2==0:
    total += element
print(total)

numbers = [3, 8, 1, 6, 7, 4]
count = 0
for element in numbers:
  if element%2==0:
    count+=1
print(count)