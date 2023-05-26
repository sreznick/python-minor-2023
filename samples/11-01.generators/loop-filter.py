
import math
source = list(range(100))
values = []
for v in source:
    if math.sin(v) <= 0:
        values.append(v)
print(values)

