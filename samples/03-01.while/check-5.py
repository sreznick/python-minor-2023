print("Введите имя")

while True:
    name = input() # вводим имя
    if name:
        break
    else:
        print("Еще раз попробуйте")

print("Hello, " + name)

