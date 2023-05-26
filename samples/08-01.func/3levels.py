a = 1

def f(a, b):
    print(a + b)
    d = a + 1
    def g(c, d):
        c1 = a + d + c
        print(c1, a, d, c)
    g(a, c)
    d += 1
    g(a, d)


c = 10
f(2, 3)

