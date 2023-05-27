def lazy_fibo():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

gen = lazy_fibo()
for _ in range(100):
    print(next(gen))
for _ in range(100):
    print(next(gen))

