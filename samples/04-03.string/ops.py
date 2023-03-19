
data = [12, 43]
print(data + [1, 2]) # [12, 43, 1, 2]
print(data * 0) # []
print(data * 1) # [12, 43]
print(data * 2) # [12, 43, 12, 43]
print(3 * (data + [1, 2])[1:3]) # [43, 1, 43, 1, 43, 1]

