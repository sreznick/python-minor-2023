def change(data, func):
    for index, value in enumerate(data):
        data[index] = func(data[index])

def square(x):
    return x * x

data = [1, 2, 3]
change(data, square)
print(data)

