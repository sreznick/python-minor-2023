n_total = 0
n_success = 0

while n_total < 10:
    name = input()
    n_total += 1

    if not name:
        continue

    n_success += 1
    print('hello, ' + name)

    if n_success == 3:
        break
else:
    print('Закончились попытки')

