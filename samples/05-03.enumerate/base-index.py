
data = [-1, 0, 3, -2, 7, 0, -2, 0, 1, -1]

for index, value in enumerate(data[5:], 5):
    if value < 0:
        print('negative at index', index)

