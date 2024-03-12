"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest

class TestCircle(unittest.TestCase):
    def setUp(self) -> None:
        self.circle = Circle(5)

    def test_add_area(self):
        """Test whether adding 2 circles' area work correctly"""
        c2 = Circle(10)
        c3 = self.circle.add_area(c2)
        radius_sq = lambda x : x.get_radius() ** 2
        self.assertAlmostEqual(radius_sq(c3), radius_sq(self.circle) + radius_sq(c2))
        self.assertAlmostEqual(self.circle.get_area() + c2.get_area(), c3.get_area())

    def test_add_area_zero_radius(self):
        """Test whether adding circle with zero radius works correctly"""
        c2 = Circle(0)
        c3 = self.circle.add_area(c2)
        self.assertEqual(c3.get_radius(), self.circle.get_radius())
        self.assertEqual(c3.get_area(), self.circle.get_area())

    def test_raise_exception_negative_radius(self):
        """Test whether the code raise exception if negative radius is inputted"""
        with self.assertRaises(Exception):
            Circle(-1)
