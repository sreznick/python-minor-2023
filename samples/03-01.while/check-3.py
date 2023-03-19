first = True
print("Введите имя")

while first or not name:
    if not first:
         print("Еще раз попробуйте")
    name = input() # вводим имя
    first = False

print("Hello, " + name)

