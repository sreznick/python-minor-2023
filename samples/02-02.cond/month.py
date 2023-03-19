n = int(input())

max_days = None
if n == 2:
    max_days = 28
elif n == 4 or n == 6 or n == 9 or n == 11:
    max_days = 30
elif n < 1 or n > 12:
    print("Bad data !!!")
else:
    max_days = 31

print(max_days)

