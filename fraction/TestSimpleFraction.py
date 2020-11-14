import unittest

from SimpleFraction import SimpleFraction

class TestSimpleFraction(unittest.TestCase):

    def test_init_with_integers(self):
        numerators = range(-2, 3) # [-2, -1, 0, 1, 2]
        denominators = range(-2, 3) # [-2, -1, 0, 1, 2]

        for numerator in numerators:
            for denominator in denominators:
                print("Testing init with valid inputs: " + str(numerator) + " " + str(denominator))
                try:
                    simple_frac = SimpleFraction(numerator, denominator)
                    self.assertTrue(simple_frac.numer == numerator and simple_frac.denom == denominator)
                except ValueError:
                    print('Integer causes value error when it shouldn\'t')

    def test_init_with_non_integers(self):
        numers_to_test = [1.5, [1], "1", True]
        denoms_to_test = [1.5, [1], "1", False]
        for numer in numers_to_test:
            print("Testing init with invalid numerator: " + str(numer))
            self.assertRaises(ValueError, SimpleFraction, numer, 1)
        
        for denom in denoms_to_test:
            print("Testing init with invalid denominator: " + str(denom))
            self.assertRaises(ValueError, SimpleFraction, 1, denom)
        
        for numer in numers_to_test:
            for denom in denoms_to_test:
                print("Testing init with invalid numer and denom: " + str(numer) + " " + str(denom))
                self.assertRaises(ValueError, SimpleFraction, numer, denom)
    
    def test_make_reciprocal(self):
        numers = range(-2, 3) # [-2, -1, 0, 1, 2]
        denoms = range(-2, 3) # [-2, -1, 0, 1, 2]
        for numer in numers:
            for denom in denoms:
                print("Testing make_reciprocal with numer and denom: " + str(numer) + " " + str(denom))
                simple_frac = SimpleFraction(numer, denom)
                recip = simple_frac.make_reciprocal()
                self.assertTrue(simple_frac.numer == recip.denom and simple_frac.denom == recip.numer)
    
    def test_validate(self):
        valid_numer = range(-2, 3) # [-2, -1, 0, 1, 2]
        valid_denom = range(-2, 3) # [-2, -1, 0, 1, 2]
        invalid_numer = [1.5, [1], "1", True]
        invalid_denom = [1.5, [1], "1", False]
        for numer in valid_numer:
            for denom in valid_denom:
                print("Testing validate with valid numer and denom: " + str(numer) + " " + str(denom))
                simple_frac = SimpleFraction(1,1)
                simple_frac.numer = numer
                simple_frac.denom = denom
                try:
                    simple_frac.validate()
                except:
                    self.assertTrue(1 == 0) 
                    # We force it to be false because
                    # if we reach this exception block
                    # that means an exeception has been thrown
                    # when it shouldn't have been
        for numer in valid_numer:
            for denom in invalid_denom:
                print("Testing validate with valid numer and invalid denom: " + str(numer) + " " + str(denom))
                simple_frac = SimpleFraction(1,1)
                simple_frac.numer = numer
                simple_frac.denom = denom
                self.assertRaises(ValueError, simple_frac.validate)

        for numer in invalid_numer:
            for denom in valid_denom:
                print("Testing validate with invalid numer and valid denom: " + str(numer) + " " + str(denom))
                simple_frac = SimpleFraction(1,1)
                simple_frac.numer = numer
                simple_frac.denom = denom
                self.assertRaises(ValueError, simple_frac.validate)
        
        for numer in invalid_numer:
            for denom in invalid_denom:
                print("Testing validate with invalid numer and invalid denom: " + str(numer) + " " + str(denom))
                simple_frac = SimpleFraction(1,1)
                simple_frac.numer = numer
                simple_frac.denom = denom
                self.assertRaises(ValueError, simple_frac.validate)
    
    def test_multiply(self):
        numers = range(-2, 3) # [-2, -1, 0, 1, 2]
        denoms = range(-2, 3) # [-2, -1, 0, 1, 2]
        invalid_multipliers = [1.5, [1], "1", True]
        simple_frac = SimpleFraction(2,3)
        for numer in numers:
            for denom in denoms:
                print("Testing multiply with two simple fractions: 2/3 * " + str(numer) + "/" + str(denom))
                new_frac = SimpleFraction(numer, denom)
                product = simple_frac.multiply(new_frac)
                self.assertTrue(product.numer == 2 * numer and product.denom == 3 * denom)
        
        for numer in numers:
            print("Testing multiply with 1 fraction and 1 integer: 2/3 * " + str(numer))
            product = simple_frac.multiply(numer)
            self.assertTrue(product.numer == 2 * numer and product.denom == 3 * numer)

        for multiplier in invalid_multipliers:
            print("Testing multiply with 1 fraction and 1 invalid multiplier: 2/3 * " + str(multiplier))
            self.assertRaises(ValueError, simple_frac.multiply, multiplier)
        

    def test_divide(self):
        numers = range(-2, 3) # [-2, -1, 0, 1, 2]
        denoms = range(-2, 3) # [-2, -1, 0, 1, 2]
        simple_frac = SimpleFraction(6, 2)
        for numer in numers:
            for denom in denoms:
                print("Testing divide with 2 fractions: 6/2 / " + str(numer) + "/" + str(denom))
                new_numer = 6 * denom
                new_denom = 2 * numer
                new_frac = SimpleFraction(numer, denom)
                quotient = simple_frac.divide(new_frac)
                self.assertTrue(quotient.numer == new_numer and quotient.denom == new_denom)

        for num in numers:
            print("Testing divide with 1 fraction and an integer: 6/2 / " + str(num))
            quotient = simple_frac.divide(num)
            self.assertTrue(quotient.denom == 2 * num)

    def test_eq(self):
        simple_frac = SimpleFraction(1,2)
        for i in range(1,11):
            print("Testing eq with equal fractions 1/2 == (1/2) * " + str(i))
            self.assertTrue(simple_frac == simple_frac.multiply(i))
        
        unequal_frac = SimpleFraction(1,3)
        print("Testing eq with unequal fractions 1/2 == 1/3")
        self.assertFalse(simple_frac == unequal_frac)

def main():
    tsf = TestSimpleFraction()
    tsf.test_init_with_integers()
    tsf.test_init_with_non_integers()
    tsf.test_make_reciprocal()
    tsf.test_validate()
    tsf.test_multiply()
    tsf.test_divide()
    tsf.test_eq()

if __name__=="__main__":
    main()