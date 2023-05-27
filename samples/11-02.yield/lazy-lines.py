def lazy_lines(name):
    with open(name, 'rt') as f:
        for line in f:
            yield line

gen1 = lazy_lines('data.txt')
print(next(gen1))
print(next(gen1))
gen2 = lazy_lines('data.txt')
print(next(gen2))
print(next(gen1))
print(next(gen2))

