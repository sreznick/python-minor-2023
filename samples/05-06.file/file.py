
with open('data.txt', 'rt') as f:
    for index, line in enumerate(f):
        line = line.strip()
        if len(line) > 10:
            print(index, line)

