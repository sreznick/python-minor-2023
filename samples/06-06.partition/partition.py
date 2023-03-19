
line = input()
id, found, details = line.partition(':')
if found:
    print('id', id)
    print('details', details)
else:
    print('no colon found')

