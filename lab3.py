# Домашнее задание 3, вариант 1
class Fraction:
    numerator = 0
    denominator = 0

    def __init__(self, numerator, denominator):
        if numerator is not None and (denominator is not None and denominator is not 0):
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = input()
            self.denominator = input()

    def inputStream(self):
        self.numerator = input()
        self.denominator = input()

    def outputStream(self):
        print(self.numerator)
        print("_")
        print(self.denominator)
