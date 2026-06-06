import unittest
from main import sum_values

class TestSumValues(unittest.TestCase):
    def test_sum_integers(self):
        self.assertEqual(sum_values([1, 2, 3, 4]), 10)
    
    def test_sum_floats(self):
        self.assertAlmostEqual(sum_values([1.5, 2.5, 3.0]), 7.0)
    
    def test_sum_mixed(self):
        self.assertAlmostEqual(sum_values([1, 2.5, 3]), 6.5)
    
    def test_empty_list(self):
        self.assertEqual(sum_values([]), 0.0)
    
    def test_negative_numbers(self):
        self.assertEqual(sum_values([-1, -2, 3]), 0)

if __name__ == '__main__':
    unittest.main()