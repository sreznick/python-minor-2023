
# В этом коде есть проблема

numbers = [123, 234, -321, 456]
i = 0
while i < len(numbers):
    print(numbers[i] - numbers[i - 1])
    i += 1

