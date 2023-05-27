def stripped(f):
    return (s.rstrip() for s in f)

with open('data1.txt', 'rt') as f:
    for s in stripped(f):
        print(s)

