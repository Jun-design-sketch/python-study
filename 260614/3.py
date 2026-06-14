list = [1, 2, 3, True, "String"] # いろんな型が入ってしまう
list.append('new')
print(list[:])

tuple = ('1', '3', '5', '7') # cannot change, packing
(one, three, *others) = tuple # unpacking
print(one, *others) # others = list

set_a = {'a', 'b', 'c'} # no index
set_b = {'x', 'y', 'c'}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))

dictionary_x = {'key1':'val1', 'key2':'val2'} # map
print(dictionary_x['key1'])