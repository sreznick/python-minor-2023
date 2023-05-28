def compare(s):
    parts = s.split()
    if len(parts) != 2:
        e = Exception('illegal # of parts')
        e.n_parts = len(parts)
        raise e
    return parts[0] == parts[1]

try:
    compare('hello world')
    compare('helloworld')
except Exception as exc:
    print("caught exception", exc, exc.n_parts)

