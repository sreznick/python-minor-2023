
# Работает, но так лучше не делать
# Лучше enumerate


data = [-1, 0, -2, 1, 1]

for i in range(len(data)):
    if data[i] < 0:
        print(i + 1)  # потому что нумерация с нуля

