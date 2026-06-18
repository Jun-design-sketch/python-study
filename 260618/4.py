some_var = 0
new_var = 1
if new_var == 1:
  print('if statement')
  some_var = 99
elif new_var == 2:
  print('if statement..')
print('outside')

for x in range(3):
  print(f'for statement {x}')

for y in range(1,4):
  print(f'range {y}')

for z in range(3,10,3):
  print(f'range step {z}')

some_li = ['apple', 'banana', 'coconut']
for a in some_li:
  print(a)
  # break
  # continue

iterator = 3
while iterator <= 5:
  print(iterator)
  iterator+=1