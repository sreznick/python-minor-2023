
data = ['apple', 'pineapple', 'mellon']
count = 0
for s in data:
    for c in s:
        if c in 'aeiouy':
            count += 1
print('found ', count, 'vowels')

