import unittest
from points import *

class Rectangle:
    """Klasa reprezentujaca prostokat na plaszczyznie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        r1 = str(self.pt1)
        r2 = str(self.pt2)
        return ("[" + r1 + ", " + r2 + "]")

    def __repr__(self):
        rect = "Rectangle(%d, %d, %d, %d)" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)
        return rect

    def __eq__(self, other):
        if(self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y):
            return 1

    def __ne__(self, other):
        return not self == other

    def center(self):
        r1 = (self.pt1.x+self.pt2.x)/2
        r2 = (self.pt1.y+self.pt2.y)/2
        return Point(r1,r2)

    def area(self):
        r1 = self.pt2.x - self.pt1.x
        r2 = self.pt2.y - self.pt1.y
        return r1*r2

    def move(self, x, y):
        self.pt1.x = self.pt1.x + x
        self.pt2.x = self.pt2.x + x
        self.pt1.y = self.pt1.y + y
        self.pt2.y = self.pt2.y + y
        return self

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.pt1, Point(2,2))
        self.assertEqual(rc.pt2, Point(4,4))
    def test_str(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(str(rc), "[(2, 2), (4, 4)]")
    def test_repr(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(repr(rc), "Rectangle(2, 2, 4, 4)")
    def test_eq(self):
        rc1 = Rectangle(2, 2, 4, 4)
        rc2 = Rectangle(2, 2, 4, 4)
        self.assertTrue(rc1.__eq__(rc2))
    def test_eq(self):
        rc1 = Rectangle(2, 2, 4, 4)
        rc2 = Rectangle(2, 6, 4, 10)
        rc3 = Rectangle(2, 2, 4, 4)
        self.assertTrue(rc1.__ne__(rc2))
        self.assertFalse(rc1.__ne__(rc3))
    def test_center(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.center(), Point(3, 3))
    def test_area(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.area(), 4)
    def test_move(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.move(2, 2), Rectangle(4, 4, 6, 6))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRectangle)
    unittest.TextTestRunner(verbosity=2).run(suite)
