
data = [12, 43, 11, 45, 34]
print(data) # [12, 43, 11, 45, 34]
data[1:3] = [5]
print(data) # [12, 5, 45, 34]
data[1:3] = [7, 8, 9]
print(data) # [12, 7, 8, 9, 34]
data[1:3] = []
print(data) # [12, 9, 34]
data[1:1] = [1, 2, 3]
print(data) # [12, 1, 2, 3, 9, 34]

