
s = 'aabb,aaa,abbb'
print(s.rpartition(',')) # ('aabb,aaa', ',', 'abbb')
print(s.rpartition(' ')) # ('', '', 'aabb,aaa,abbb')
print(s.rpartition('ab')) # ('aabb,aaa,', 'ab', 'bb')

