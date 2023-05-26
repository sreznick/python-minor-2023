def print_call(f):

    def worker(p):
        print("call function with ", p)
        return f(p)

    return worker

def incr(v):
    return v + 1

incr = print_call(incr)

print(incr(5))

