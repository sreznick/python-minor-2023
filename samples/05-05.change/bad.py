
data = ['apple', 'pineapple', 'mellon']
for s in data:
    if s[0] == 'a':
        data[len(data):] = [s]

