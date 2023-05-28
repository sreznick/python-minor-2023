class EmptyListException(Exception):

    def __init__(self):
        super().__init__(self, "List is empty")

class IllegalElementException(Exception):

    def __init__(self, index, value):
        super().__init__(self, f"illegal element at index {index}")
        self._index = index
        self._value = value


def str_mean(s):
    def convert(index, word):
        try:
            return int(word)
        except ValueError:
            raise IllegalElementException(index, word)

    if not s:
        raise EmptyListException()
    words = s.split()
    if not words:
        raise EmptyListException()

    return sum(convert(index, w) for index, w in enumerate(words)) / len(words)


def f(s):
    try:
        print(str_mean(s))
    except Exception as exc:
        print('caught', exc)

f('')
f('123 45')
f('iq123 45')

