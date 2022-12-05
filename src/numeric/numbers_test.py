import unittest

from numeric.numbers import add


class NumbersTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(1, 4))


if __name__ == '__main__':
    unittest.main()
