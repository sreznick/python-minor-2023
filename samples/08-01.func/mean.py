def mean(*values):
    total = 0
    for v in values:
        total += v
    return total / len(values)

print(mean(1))
print(mean(2, 3))
print(mean(1, 5, 123))

