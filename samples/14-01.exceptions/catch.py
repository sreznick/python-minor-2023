def f():
    print('abc')
    try:
        raise Exception('I am exception')
    except:
        print("caught exception")
    print('bcd')

print(123)
f()
print(234)

