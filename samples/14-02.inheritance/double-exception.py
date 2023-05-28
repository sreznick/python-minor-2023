try:
    try:
        int('dcqdcqc')
    finally:
        print(1/0)
except Exception as exc:
    print('got', exc)

