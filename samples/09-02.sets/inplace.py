names_1 = {'vasya', 'petya', 'dima'}
names_2 = {'petya', 'kolya', 'sasha', 'dima'}
names_1.update(names_2)
print(names_1)

names_1 = {'vasya', 'petya', 'dima'}
names_2 = {'petya', 'kolya', 'sasha', 'dima'}
names_2.intersection_update(names_1)
print(names_2)

names_1 = {'vasya', 'petya', 'dima'}
names_2 = {'petya', 'kolya', 'sasha', 'dima'}
names_1.difference_update(names_2)
print(names_1)

names_1 = {'vasya', 'petya', 'dima'}
names_2 = {'petya', 'kolya', 'sasha', 'dima'}
names_2.symmetric_difference_update(names_1)
print(names_2)

