class EmptyListException(Exception):

    def __init__(self):
        super().__init__(self, "List is empty")

class IllegalElementException(Exception):

    def __init__(self, index, value):
        super().__init__(self, f"illegal element at index {index}")
        self._index = index
        self._value = value

