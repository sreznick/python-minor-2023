a, b = 1, 2
print("a", a) # a 1
print("b", b) # b 2

a, b = b, a
print("a", a) # a 2
print("b", b) # b 1

c = 1, 2
print("c", c) # c (1, 2)

a, b = c[::-1]
print("a", a) # a 2
print("b", b) # b 1

a, b = c, (a, b)
print("a", a) # a (1, 2)
print("b", b) # b (2, 1)

