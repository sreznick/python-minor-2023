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


str_mean('123 qwerty')

