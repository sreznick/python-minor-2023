def adder(delta):
    return lambda v: v + delta

incr = adder(1)
add_5 = adder(5)
print(incr(10))
print(add_5(10))

