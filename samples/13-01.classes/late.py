class Text:
    def __init__(self, data):
        self._data = data
        self._n_words = None

    def get_data(self):
        return self._data

    def n_words(self):
        if self._n_words is None:
            self._n_words = len(self._data.split())
        return self._n_words


t = Text("To be or not to be")
print("t", t.get_data())
print("t", t.n_words())

