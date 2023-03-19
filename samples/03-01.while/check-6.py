print("Введите имя")

while True:
    name = input() # вводим имя
    if name:
        break
    print("Еще раз попробуйте")

print("Hello, " + name)

