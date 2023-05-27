def f():
    print('abc')
    raise Exception('I am exception')
    print('bcd')

print(123)
try:
    f()
except:
    print("caught exception")
print(234)

