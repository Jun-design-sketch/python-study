lis = [1,2,3,4,5]
t_comp = [el for el in lis if el > 2]
print(t_comp)

lll = [5, 7, 9, 16, 77, 2, 1]
stream = [element for element in lll if element % 2 == 1]
print(stream)

def this_is_func(*arg):
  print('see indent')
  print(arg)
  return 99
integer = this_is_func('ok');
this_is_func('a','b','c')
print(integer)

# input_arg = input('type any word')
# print(input_arg)

f = open('test.txt', 'w', encoding='utf8')
f.write('1\n')
f.write('2\n')
f.write('3\n')
f.close

f = open('test.txt','r', encoding='utf8')
con = f.read()
print(con)
f.close

with open('new_test.txt', 'w', encoding='utf8') as sheet:
  sheet.write('A1')
  sheet.write('B2')
  sheet.write('C3')
# no need to close