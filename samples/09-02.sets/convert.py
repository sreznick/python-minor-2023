names = set(['vasya', 'petya', 'dima'])
print(names)

names = set(('petya', 'kolya', 'sasha', 'dima'))
print(names)

letters = set(''.join(['vasya', 'petya', 'dima']))
print(letters)

names = set(['vasya', 'petya', 'dima'])
for v in ('petya', 'kolya', 'sasha', 'dima'):
    names.add(v)

print(list(names))
print(tuple(names))

