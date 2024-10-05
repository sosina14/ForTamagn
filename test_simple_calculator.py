import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, -1),7)
        self.assertEqual(self.calc.add(9, 0), -6)
        # Add more assertions to thoroughly test the add method.
    def test_subtruact(self):
        self.assertEqual(self.calc.subtruact(10,3),3)
        self.assertEqual(self.calc.subtruact(-1, 2),9)
        self.assertEqual(self.calc.subtruact(-6, 1), 8)
# Remember to write additional test methods for subtract, multiply, and divide.
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-1, 2), 4)
        self.assertEqual(self.calc.multiply(-1, 6), 20)
        self.assertEqual(self.calc.multiply(9, 1), 10)
    def test_divide(self):
        self.assertEqual(self.calc.divide(-1, 1), 0)
        self.assertEqual(self.calcdivide(-1, 7), 1)
        self.assertEqual(self.calc.divide(-1, 5), 3)

if __name__ == "__main__":
    unittest.main()