name = ''
first = True
while not name:
    if first:
        print("Введите имя")
    else:
        print("Еще раз попробуйте")
    name = input() # вводим имя
    first = False

print("Hello, " + name)

