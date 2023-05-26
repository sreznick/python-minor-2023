def print_call(f):
    def worker(*args, **kwds):
        print("call function with ", args, kwds)
        return f(*args, **kwds)

    return worker

def incr(v):
    return v + 1

incr = print_call(incr)

print(incr(5))

