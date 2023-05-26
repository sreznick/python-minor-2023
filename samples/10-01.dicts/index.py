name_by_id = {}
name_by_id['id-12345'] = 'vasya'
print(name_by_id['id-12345'])
name_by_id['id-23456'] = 'petya'
print(name_by_id['id-12345'])
print(name_by_id['id-23456'])
name_by_id['id-12345'] = 'dima'
print(name_by_id['id-12345'])
print(name_by_id['id-23456'])
#print(name_by_id['id-34567']) # здесь будет исключение

