import unittest
from points import *

class Rectangle:
    """Klasa reprezentujaca prostokat na plaszczyznie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if x1 == x2 and y1 == y2:
            raise ValueError('Nie moga byc te same punkty')
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
        if not isinstance(other, Rectangle):
            raise ValueError("Can not compare")
        if(self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y and self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y):
            return 1

    def __ne__(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Can not compare")
        return not self == other

    @property
    def center(self):
        r1 = (self.pt1.x+self.pt2.x)/2
        r2 = (self.pt1.y+self.pt2.y)/2
        return Point(r1,r2)

    def area(self):
        r1 = self.pt2.x - self.pt1.x
        r2 = self.pt2.y - self.pt1.y
        return r1*r2

    def move(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError("x and y must be int value")
        self.pt1.x = self.pt1.x + x
        self.pt2.x = self.pt2.x + x
        self.pt1.y = self.pt1.y + y
        self.pt2.y = self.pt2.y + y
        return self

    def intersection(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("arg must be Ractangle")
        return Rectangle(
                max(self.pt1.x, other.pt1.x),
                max(self.pt1.y, other.pt1.y),
                min(self.pt2.x, other.pt2.x),
                min(self.pt2.y, other.pt2.y)
                )

    def cover(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("arg must be Ractangle")
        return Rectangle(
                min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y),
                max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y)
        )

    def make4(self):
        return [
        Rectangle(self.center.x, self.center.y, self.pt2.x, self.pt2.y),
        Rectangle(self.center.x, self.pt1.y, self.pt2.x, self.center.y),
        Rectangle(self.pt1.x, self.center.y, self.center.x, self.pt2.y),
        Rectangle(self.pt1.x, self.pt1.y, self.center.x, self.center.y)
        ]

        return [rect1, rect2, rect3, rect4]

class TestRectangle(unittest.TestCase):
    def test_init(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.pt1, Point(2,2))
        self.assertEqual(rc.pt2, Point(4,4))
    def test_init_raise(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 2, 2)
    def test_str(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(str(rc), "[(2, 2), (4, 4)]")
    def test_repr(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(repr(rc), "Rectangle(2, 2, 4, 4)")
    def test_eq(self):
        rc1 = Rectangle(2, 2, 4, 4)
        rc2 = Rectangle(2, 2, 4, 4)
        self.assertTrue(rc1 == rc2)
    def test_eq_raise(self):
        with self.assertRaises(ValueError):
           Rectangle(2, 2, 4, 4) == 2
    def test_ne(self):
        rc1 = Rectangle(2, 2, 4, 4)
        rc2 = Rectangle(2, 6, 4, 10)
        rc3 = Rectangle(2, 2, 4, 4)
        self.assertTrue(rc1 != rc2)
        self.assertFalse(rc1 != rc3)
    def test_ne_raise(self):
        with self.assertRaises(ValueError):
           Rectangle(2, 2, 4, 4) != 2
    def test_center(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.center, Point(3, 3))
    def test_area(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.area(), 4)
    def test_move(self):
        rc = Rectangle(2, 2, 4, 4)
        self.assertEqual(rc.move(2, 2), Rectangle(4, 4, 6, 6))
    def test_move_raise(self):
        with self.assertRaises(ValueError):
           Rectangle(2, 2, 4, 4).move(2,"s")
        with self.assertRaises(ValueError):
           Rectangle(2, 2, 4, 4).move("s",6)
    def test_intersection(self):
        rc1 = Rectangle(2,2,7,4)
        rc2 = Rectangle(1,1,3,5)
        self.assertEqual(rc1.intersection(rc2), Rectangle(2,2,3,4))
    def test_intersection_raise(self):
        rc1 = Rectangle(2,2,7,4)
        rc2 = Rectangle(1,1,3,5)
        with self.assertRaises(ValueError):
           rc1.intersection("ssss")
    def test_cover(self):
        rc1 = Rectangle(2,2,7,4)
        rc2 = Rectangle(1,1,3,5)
        self.assertEqual(rc1.cover(rc2), Rectangle(1,1,7,5))
    def test_cover_raise(self):
        rc1 = Rectangle(2,2,7,4)
        rc2 = Rectangle(1,1,3,5)
        with self.assertRaises(ValueError):
           rc1.cover("ssss")
    def test_make4(self):
        four = Rectangle(1,1,5,5).make4()
        self.assertEqual(four[0], Rectangle(3,3,5,5))
        self.assertEqual(four[3], Rectangle(1,1,3,3))
        self.assertEqual(four[1], Rectangle(3,1,5,3))
        self.assertEqual(four[2], Rectangle(1,3,3,5))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRectangle)
    unittest.TextTestRunner(verbosity=2).run(suite)

