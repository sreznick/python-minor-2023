name_by_id = {}
for k in name_by_id:
    print(k)
print()

name_by_id['id-12345'] = 'vasya'
for k in name_by_id:
    print(k)
print()

name_by_id['id-23456'] = 'petya'
for k in name_by_id:
    print(k)
print()

del name_by_id['id-12345']
name_by_id['id-12345'] = 'dima'
for k in name_by_id:
    print(k)

