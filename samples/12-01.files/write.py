import sys

with open('data2.txt', 'wt') as f:
    f.write('Hello, world\n')

with open('data3.txt', 'wt') as f:
    print('Hello, world', file=f)

sys.stdout.write('Hello, world\n')

