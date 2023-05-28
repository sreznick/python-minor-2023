print('before fibo: ', __name__)
def fibo(n):
    print('fibo', __name__)
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return prev

print('after fibo', __name__)

