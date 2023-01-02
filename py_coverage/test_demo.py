import unittest
from demo import CalcDemo

class TestDemo(unittest.TestCase):

    def test_plus(self):
        self.assertEquals(CalcDemo(6, 4).plus(), 10)

    def test_subtract(self):
        self.assertEquals(CalcDemo(6, 4).subtract(), 2)

    def test_multiply(self):
        self.assertEquals(CalcDemo(6, 4).multiply(), 24)


if __name__ == '__main__':
    unittest.main(verbosity=2)