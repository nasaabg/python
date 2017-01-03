import unittest

class Stack:
    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementow na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.n == self.size:
            raise IndexError
        self.items[self.n] = data
        self.n = self.n + 1

    def pop(self):
        if self.is_empty():
            raise IndexError
        self.n = self.n - 1
        data = self.items[self.n]
        self.items[self.n] = None  # usuwam referencje
        return data

class Test(unittest.TestCase):
    def setUp(self):
        self.size = 15
        self.stack = Stack(self.size)

    def testemptyTest(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(2)
        self.assertFalse(self.stack.is_empty())

    def testfullTest(self):
        self.assertFalse(self.stack.is_full())
        for x in range(0,self.size,1):
            self.stack.push(x+10)
        self.assertTrue(self.stack.is_full())

    def testpushTest(self):
        for x in range(0,self.size-1,1):
            self.stack.push(x+10)
        self.stack.push(10)
        self.assertRaises(IndexError, lambda: self.stack.push(100))

    def testpopTest(self):
        for x in range(0,self.size,1):
            self.stack.push(x+20)
        for x in range(self.size):
            self.stack.pop()
        self.assertRaises(IndexError, lambda: self.stack.pop())	

if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
