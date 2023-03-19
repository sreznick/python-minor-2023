
with open('data.txt', 'rt') as f:
    for index, line in enumerate(f):
        print(index, line, end='')

