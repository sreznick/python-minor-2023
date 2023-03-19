
def f(a=20, b=50, /, c=100):
    print(a + b + c)

f()
f(1)
f(1, 2)
f(1, c=2)
f(1, 2, 3)
f(1, 2, c=3)

