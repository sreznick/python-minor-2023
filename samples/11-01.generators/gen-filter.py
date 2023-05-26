import math
source = list(range(100))
values = [v for v in source if math.sin(v) <= 0]
print(values)

