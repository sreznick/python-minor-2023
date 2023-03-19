
data = [[12, 43], [11, 22]]
print(data) # [[12, 43], [11, 22]]
data2 = data[:]
print(data2) # [[12, 43], [11, 22]]
data[1] = [33, 44]
print(data) #  [[12, 43], [33, 44]]
print(data2) # [[12, 43], [11, 22]]
data[0][0] = 55
print(data) #  [[55, 43], [33, 44]]
print(data2) # [[55, 43], [11, 22]]


print(data is data2) # False
print(data[0] is data2[0]) # True

