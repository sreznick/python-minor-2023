a = 1

def f(b, c):
    global a
    a = b ** c
    print(a + b)
    d = a + 1
    print(c)

print(a) # 1
f(2, 3)
print(a) # 8

