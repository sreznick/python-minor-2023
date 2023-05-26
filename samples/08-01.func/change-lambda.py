
def change(data, func):
    for index, value in enumerate(data):
        data[index] = func(data[index])

data = [1, 2, 3]
change(data, lambda x: x * x)
print(data)

