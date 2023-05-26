user = ('vasya', 'id-1234567', (10, 5, 2001))

name, id, (day, month, year) = user
print(name, id, day, month)

name, _, (day, _, year) = user
print(name, day, year)

name, id, birthdate = user
print(name, id, birthdate)

