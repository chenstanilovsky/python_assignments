class SimpleFraction:
    def __init__(self, numerator, denominator):
        if not type(numerator) is int or not type(denominator) is int:
            raise ValueError

        self.numer = numerator
        self.denom = denominator

    def make_reciprocal(self):
        reciprocal = SimpleFraction(self.denom, self.numer)
        return reciprocal
    
    def validate(self):
        if not type(self.numer) is int or not type(self.denom) is int:
            raise ValueError

    def multiply(self, other):
        if not type(other) is int and not type(other) is SimpleFraction:
            raise ValueError

        product = None

        if type(other) is int:
            product = SimpleFraction(self.numer * other, self.denom * other)
        elif type(other) is SimpleFraction:
            product = SimpleFraction(self.numer * other.numer, self.denom * other.denom)

        return product
    
    def divide(self, other):
        if not type(other) is int and not type(other) is SimpleFraction:
            raise ValueError
        
        quotient = None
        if type(other) is int:
            quotient = SimpleFraction(self.numer, self.denom * other)
        if type(other) is SimpleFraction:
            quotient = self.multiply(other.make_reciprocal())
        return quotient

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)
    
    def __eq__(self, other):
        val_self = self.numer / self.denom
        val_other = other.numer / other.denom

        if val_self == val_other:
            return True
        return False
