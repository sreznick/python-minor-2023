def f():
    print('abc')
    raise Exception('I am exception')
    print('bcd')

print(123)
f()
print(234)

