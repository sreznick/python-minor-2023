def print_user(name, address, **kwds):
    print("User name:", name)
    if address is not None:
        print("Address:", address)
    else:
        print("Address is absent")
    for k, v in kwds.items():
        print(k + ":", v)

print_user('vasya', 'moscow')
print_user('vasya', None, age=23, salary=11111)

