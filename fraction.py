class Fraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + ' / ' + str(self.denominator)

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __add__(self, other):
        numeratorNew = other.getDenominator() * self.getNumerator() + \
            other.getNumerator() * self.getDenominator()
        denominatorNew = other.getDenominator() * self.getDenominator()
        return Fraction(numeratorNew, denominatorNew)


myFraction = Fraction(3, 4)
anotherFraction = Fraction(1, 8)
print(myFraction)
print(myFraction.getNumerator())
print(myFraction + anotherFraction)
