
data = [-1, 0, -2, 1, 1]

for pair in enumerate(data):
    index, value = pair
    if value < 0:
        print(index + 1, value)  # потому что нумерация с нуля

for index, value in enumerate(data):
    if data[index] < 0:
        print(index + 1, value)  # потому что нумерация с нуля

