def print_call(f):
    def worker(*args, **kwds):
        print("call function with ", args, kwds)
        return f(*args, **kwds)

    return worker

def sum(a, b):
    return a + b

sum = print_call(sum)

print(sum(5, 10))
print(sum(a=5, b=10))

