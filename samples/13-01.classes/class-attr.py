class Text:

    VOWELS = 'auioey'

    def __init__(self, data):
        self._data = data
        self._n_vowels = None

    def get_data(self):
        return self._data

    def n_vowels(self):
        if self._n_vowels is None:
            self._n_vowels = sum(1 for c in self._data if c in Text.VOWELS)
        return self._n_vowels


t = Text("To be or not to be")
print("t", t.get_data())
print("t", t.n_vowels())

