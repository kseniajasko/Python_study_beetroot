# Create a Fraction class, which will represent all basic arithmetic
# logic for fractions (+, -, /, *) with appropriate checking and error handling

class Fraction:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type for operand')
        return Fraction(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type for operand')
        return Fraction(self.value - other.value)

    def __mul__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type for operand')
        return Fraction(self.value*other.value)

    def __truediv__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('wrong type for operand')
        return Fraction(self.value/other.value)

    def __str__(self):
        return f"Fraction: {self.value}"

    def __repr__(self):
        return self.__str__()

x = Fraction(1/2)
y = Fraction(5/8)
z = Fraction(2/5)

print(x+y+z)
print(x-y-z)
print(y*z)
print(z/y)