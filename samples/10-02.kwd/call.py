def print_user(name, address, **kwds):
    print("User name:", name)
    if address is not None:
        print("Address:", address)
    else:
        print("Address is absent")
    for k, v in kwds.items():
        print(k + ":", v)


data = {'name': 'vasya', 'address': 'qwerty', 'hobby': 'python'}
print_user(**data)

