
s = 'aabb,aaa,abbb'
print(s.removeprefix('a')) # 'abb,aaa,abbb'
print(s.removeprefix('aa')) # 'bb,aaa,abbb'
print(s.removeprefix('aab')) # 'b,aaa,abbb'
print(s.removeprefix('aaa')) # 'aabb,aaa,abbb'
print(s.removesuffix('b')) # 'aabb,aaa,abb'
print(s.removesuffix('abbb')) # 'aabb,aaa,'
print(s.removesuffix('aab')) # 'aabb,aaa,abbb'

