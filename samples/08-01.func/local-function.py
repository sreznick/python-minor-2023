def fibo(n):
    def helper(curr, prev, n):
        if n == 0:
            return prev
        return helper(curr + prev, curr, n - 1)

    return helper(1, 0, n)

print(fibo(0)) # 0
print(fibo(1)) # 1
print(fibo(2)) # 1
print(fibo(3)) # 2
print(fibo(4)) # 3
print(fibo(5)) # 5

