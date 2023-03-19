
print('vasya petya dima'.split(' ')) # ['vasya', 'petya', 'dima']
print('vasya  petya   dima'.split(' ', 3)) # ['vasya', '', 'petya', '  dima']
print('vasya  petya   dima'.split()) # ['vasya', 'petya', 'dima']
print('vasya  petya   dima'.split(None)) # ['vasya', 'petya', 'dima']
print('vasya  petya   dima'.split(None, 2)) # ['vasya', 'petya', 'dima']

