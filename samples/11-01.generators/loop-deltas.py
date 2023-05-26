source = [1, 10, 2, 2.9, 1.2]
deltas = []
for v1, v2 in zip(source, source[1:]):
    deltas.append(v2 - v1)
print(deltas)

