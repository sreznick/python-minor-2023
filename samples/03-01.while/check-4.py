print("Введите имя")
name = ''

while not name:
    name = input() # вводим имя
    if not name:
        print("Еще раз попробуйте")

print("Hello, " + name)

