
with open('data1.txt', 'rt') as f1:
    with open('data2.txt', 'rt') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                print(line1, end='')
                print(line2, end='')
                print()

