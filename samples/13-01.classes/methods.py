class Text:
    def __init__(self, data):
        self._data = data
        self._n_words = len(data.split())

    def get_data(self):
        return self._data

    def n_words(self):
        return self._n_words


t = Text("To be or not to be")
print("t", t.get_data())
print("t", t.n_words())

