def hello():
    print('started to work')
    return "hello"

def hello_lazy():
    print('started to work')
    yield "hello"
    print('continue to work')


print('call hello')
s = hello()
print(s)
print('call hello_lazy')
gen = hello_lazy()
print(gen)
print(next(gen))
#next(gen)

