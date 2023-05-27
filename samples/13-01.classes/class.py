class Text:
    print("define Text")

    def __init__(self, data):
        print("init. self:", self)
        print("init. data:", data)

print("start")
t = Text("To be or not to be")
print("t", t)

