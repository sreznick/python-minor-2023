def lazy_hello():
    yield "hello"

def lazy_map(data, f):
    gen = iter(data)
    while True:
        yield f(next(gen))

gen = lazy_map(lazy_hello(), len)
print(next(gen))

gen = lazy_map(['q', 'qwerty'], len)
print(next(gen))
print(next(gen))

