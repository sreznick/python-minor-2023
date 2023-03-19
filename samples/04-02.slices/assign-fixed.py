
data = [12, 43, 11]
print(data) #  [12, 43, 11]
data2 = data[:]
print(data == data2) # True
print(data2) #  [12, 43, 11]
data[1] = 0
print(data) #  [12, 0, 11]
print(data2) #  [12, 43, 11]
print(data is data2) # False
print(data == data2) # False

