
print('vasya,petya,dima'.split(',')) # ['vasya', 'petya', 'dima']
print('vasya,petya,dima'.split(', ')) # ['vasya,petya,dima']
print('vasya, petya,dima'.split(', ')) # ['vasya', 'petya,dima']
print('vasya,petya,dima'.split(',', -1)) # ['vasya', 'petya', 'dima']
print('vasya,petya,dima'.split(',', 0)) # ['vasya,petya,dima']
print('vasya,petya,dima'.split(',', 1)) # ['vasya', 'petya,dima']
print('vasya,petya,dima'.split(',', 2)) # ['vasya', 'petya', 'dima']
print('vasya,petya,dima'.split(',', 3)) # ['vasya', 'petya', 'dima']

