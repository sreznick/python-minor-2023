v1 = 5
def f(a):
    print('f', v1, a)
    v2 = v1 + a

    def g(b):
        print('g', v1, v2, a)
        v3 = v1 + v2 + a
        f(5)

    if a == 0:
        g(1)

print('start')
f(0)
print('finish')

