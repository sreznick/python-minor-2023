def counter(start, step):
    state = start

    def incr():
        nonlocal state
        state += step

    return incr, lambda : state

adder_1, getter_1 = counter(10, 2)
adder_2, getter_2 = counter(5, 1)
adder_1()
adder_1()
print(getter_1())
adder_2()
print(getter_2())

