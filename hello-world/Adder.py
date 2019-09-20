import unittest


class TestSum(unittest.TestCase):

    def product(self, x, y):
        return x * y

    def test_product(self):
        self.assertEqual(self.product(4, 4), 16, "Should be 6")

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")


if __name__ == '__main__':
    unittest.main()
