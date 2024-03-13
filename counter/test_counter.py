import unittest
from counter import Counter

class TestCounter(unittest.TestCase):
    def setUp(self) -> None:
        self.a = Counter()
        self.b = Counter()

    def test_singleton_reference(self):
        self.assertIs(self.a, self.b)
        self.assertEqual(id(self.a), id(self.b))

    def test_increment(self):
        for _ in range(3):
            self.a.increment()
            self.b.increment()
        c = Counter()
        self.assertEqual(self.a.count, self.b.count, 6)
        self.assertEqual(self.a.count, self.b.count, c.count)
        self.assertEqual(c.count, 6)
        self.assertIs(c, self.a, self.b)
        self.assertEqual(id(c), id(self.a), id(self.b))
