import unittest
class Queue:
    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise IndexError
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise IndexError
        data = self.items[self.head]
        self.items[self.head] = None  # usuwam referencje
        self.head = (self.head + 1) % self.n
        return data

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.size = 15
        self.queue = Queue(self.size)
    def testFULL(self):
        self.assertFalse(self.queue.is_full())
        for x in range(self.size):
            self.queue.put(x)
        self.assertTrue(self.queue.is_full())
        self.queue.get()
        self.assertFalse(self.queue.is_full())
    def testEMPTY(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(1)
        self.assertFalse(self.queue.is_empty())
        self.queue.get()
        self.assertTrue(self.queue.is_empty())
    def testPUT(self):
        self.assertTrue(self.queue.is_empty())
        for x in range(self.size):
            self.queue.put(x+10)
        self.assertTrue(self.queue.is_full())
        self.assertRaises(IndexError, lambda: self.queue.put(1000))
    def testGET(self):
        self.assertRaises(IndexError, lambda: self.queue.get())
        self.assertRaises(IndexError, lambda: self.queue.get())
        self.assertRaises(IndexError, lambda: self.queue.get())
        self.queue.put(2+10)
        self.queue.get()
        self.assertRaises(IndexError, lambda: self.queue.get())
        for x in range(self.size-1):
            self.queue.put(x+10)
        for x in range(self.size - 1):
            self.queue.get()
        self.assertRaises(IndexError, lambda: self.queue.get())
if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
