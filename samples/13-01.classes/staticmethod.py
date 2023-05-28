class Rational:

    def __init__(self, p, q):
        self._p = p
        self._q = q

    @staticmethod
    def integer(value):
        return Rational(value, 1)


print(Rational.integer(10))


