with open('in.txt') as fin:
    with open('out.txt', 'wt') as fout:
        while True:
            s = fin.readline()
            if not s:
                break
            fout.write(str(int(s) ** 0.5) + '\n')

