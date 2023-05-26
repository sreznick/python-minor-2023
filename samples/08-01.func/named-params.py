def f(*, a=20, b=50, c=100):
    print(a + b + c)

f()
f(c=1)
f(a=1)
f(b=1)
f(b=1, a=2)
f(a=1, c=2)
f(a=1, b=2, c=3)

