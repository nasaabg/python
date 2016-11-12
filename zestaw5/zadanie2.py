# Jan Kurzydło
import unittest
import math

def frac(licznik, mianownik):
    if mianownik == 0:
        return "Mianownik nie moze byc 0"
    elif(licznik % mianownik == 0):
        licznik=licznik/mianownik
        mianownik = 1
    else :
        gcd = math.gcd(licznik, mianownik)
        licznik = licznik / gcd
        mianownik = mianownik / gcd

    L=[licznik, mianownik]
    return L

# frac1 + frac2
def add_frac(frac1, frac2):
    licznik = (frac1[0]*frac2[1]) + (frac2[0]*frac1[1])
    mianownik = (frac1[1]*frac2[1])
    return frac(licznik,mianownik)

# frac1 - frac2
def sub_frac(frac1, frac2):
   licznik = (frac1[0]*frac2[1]) - (frac2[0]*frac1[1])
   mianownik = (frac1[1]*frac2[1])
   return frac(licznik,mianownik)

# frac1 * frac2
def mul_frac(frac1, frac2):
    licznik = frac1[0]*frac2[0]
    mianownik = frac1[1]*frac2[1]
    return frac(licznik,mianownik)

# frac1 / frac2
def div_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1]
    mianownik = frac1[1] * frac2[0]
    return frac(licznik,mianownik)

# is pisitive
def is_positive(frac):
    if frac[0] > 0 and frac[1] > 0:
        return True
    elif frac[0] < 0 and frac[1] < 0:
        return True
    else:
        return False

# is zero
def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False

def cmp_frac(frac1, frac2):
    if frac2float(frac1) < frac2float(frac2):
        return -1
    elif frac2float(frac1) == frac2float(frac2):
        return 0
    elif frac2float(frac1) > frac2float(frac2):
        return 1

# to float
def frac2float(frac):
    return frac[0] / float(frac[1])

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 4]), [3, 4])
    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 8]), [3, 8])
    def test_mul_frac(self):
        self.assertEqual(mul_frac([3, 4], [2, 3]), [1, 2])
    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
    def test_is_positive(self):
        self.assertEqual(is_positive([2, 3]), True)
        self.assertEqual(is_positive([2, -3]), False)
        self.assertEqual(is_positive([-2, 3]), False)
        self.assertEqual(is_positive([-2, -3]), True)
    def test_is_zero(self):
        self.assertEqual(is_zero([0, -5]), True)
        self.assertEqual(is_zero([3, -4]), False)
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([5, 9], [6, 9]), -1)
        self.assertEqual(cmp_frac([5, 9], [5, 9]), 0)
        self.assertEqual(cmp_frac([6, 9], [5, 9]), 1)
    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
    def tearDown(self):
        self.zero[:] = []

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
