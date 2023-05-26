name_by_id = {}
print(name_by_id.get('id-12345')) # None
print(name_by_id.get('id-12345', '')) # ''
name_by_id['id-12345'] = 'vasya'
print(name_by_id.get('id-12345')) # 'vasya'
print(name_by_id.get('id-12345', '')) # 'vasya'
print(name_by_id.get('id-23456')) # None
print(name_by_id.get('id-123456', '')) # ''

