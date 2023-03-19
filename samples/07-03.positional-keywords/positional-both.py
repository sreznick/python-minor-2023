
def incr(v, /, delta):
    return v + delta

print(incr(5, 3))
#print(incr(v=5, delta=3))  # некорректно
print(incr(5, delta=3))

