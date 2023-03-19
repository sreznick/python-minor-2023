n_total = 0
n_success = 0
found_break = False

while n_total < 10:
    name = input()
    n_total += 1

    if not name:
        continue

    n_success += 1
    print('hello, ' + name)

    if n_success == 3:
        found_break = True
        break

if not found_break:
    print('Закончились попытки')

