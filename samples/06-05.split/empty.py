
print(',vasya,petya,dima'.split(',')) # ['', 'vasya', 'petya', 'dima']
print(',vasya,petya,dima'.split(',', 1)) # ['', 'vasya,petya,dima']
print(' vasya, petya,dima'.split(' ')) # ['', 'vasya,', 'petya,dima']
print('  vasya '.split(' ')) # ['', '', 'vasya', '']
print(' '.split(' ')) # ['', '']
print('  '.split(' ')) # ['', '', '']
print('hello  world'.split(' ')) # ['hello', '', 'world']

