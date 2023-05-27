with open('data1.txt', 'rt') as f:
    s = f.readline()
    print(s)
    s = f.readline()
    print(s[::2])

