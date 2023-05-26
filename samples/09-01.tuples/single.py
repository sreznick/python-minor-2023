a = 1,
print("a", a) # a (1,)

a, = 1,
print("a", a) # a 1

data = (5, 10, 20)
a = data[:1]
print("a", a) # a (5,)

a, = data[:1]
print("a", a) # a 5

