def compare(s):
    parts = s.split()
    if len(parts) != 2:
        raise Exception(len(parts))
    return parts[0] == parts[1]

try:
    compare('hello world')
    compare('helloworld')
except Exception as exc:
    print("caught exception", exc)

