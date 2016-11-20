import math
import unittest

class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    # konstruktor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # zwraca string "(x, y)"
    def __str__(self):
        S = "(%d, %d)" % (self.x, self.y)
        return S

    # zwraca string "Point(x, y)"
    def __repr__(self):
        S = "Point(%d, %d)" % (self.x, self.y)
        return S

   # obsluga point1 == point2
    def __eq__(self, other):
        if(self.x == other.x and self.y == other.y):
            return 1

    # obsluga point1 != point2
    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x+other.x, self.y+other.y)
    def __sub__(self, other):  # v1 - v2
        return Point(self.x-other.x, self.y-other.y)
    def __mul__(self, other):  # v1 * v2, iloczyn skalarny
        return self.x * other.x + self.y * other.y
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x
    def length(self):          # dlugosc wektora
        a = math.pow(self.x, 2)
        b = math.pow(self.y, 2)
        result = math.sqrt(a+b)
        return result

class TestPoint(unittest.TestCase):
    def test_init(self):
        point = Point(2, 3)
        self.assertEqual(point.x, 2)
        self.assertEqual(point.y, 3)
    def test_default_init(self):
        point = Point()
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)
    def test_str(self):
        point = Point(2, 4)
        self.assertEqual(str(point), "(2, 4)")
    def test_repr(self):
        point = Point(2, 4)
        self.assertEqual(repr(point), "Point(2, 4)")
    def test_eq(self):
        point1 = Point(2,4)
        point2 = Point(2,4)
        self.assertTrue(point1.__eq__(point2))
    def test_ne(self):
        point1 = Point(2,4)
        point2 = Point(2,3)
        point3 = Point(2,4)
        self.assertTrue(point1.__ne__(point2))
        self.assertFalse(point1.__ne__(point3))
    def test_add(self):
        point1 = Point(2,4)
        point2 = Point(2,3)
        self.assertEqual(point1.__add__(point2), Point(4, 7))
    def test_sub(self):
        point1 = Point(2,4)
        point2 = Point(2,4)
        self.assertEqual(point1.__sub__(point2), Point(0, 0))
    def test_mul(self):
        point1 = Point(2,4)
        point2 = Point(2,4)
        self.assertEqual(point1.__mul__(point2), 20)
    def test_cross(self):
        point1 = Point(2,4)
        point2 = Point(2,4)
        self.assertEqual(point1.cross(point2), 0)
    def test_length(self):
        point1 = Point(6,8)
        self.assertEqual(point1.length(), 10)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPoint)
    unittest.TextTestRunner(verbosity=2).run(suite)
