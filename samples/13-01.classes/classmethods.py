class Text:

    VOWELS = 'auioey'

    def __init__(self, data):
        self._data = data
        self._n_vowels = None

    @classmethod
    def print_settings(self):
        print(self.VOWELS)


Text.print_settings()

