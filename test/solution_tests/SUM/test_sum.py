import unittest

from solutions.SUM import sum_solution


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_solution.compute(1, 2), 3)
        self.assertEqual(sum_solution.compute(100, 100), 200)
        self.assertEqual(sum_solution.compute(0, 0), 0)
        self.assertEqual(sum_solution.compute(34, 12), 46)
        self.assertEqual(sum_solution.compute(64, 56), 120)
        self.assertEqual(sum_solution.compute(87, 34), 121)


if __name__ == '__main__':
    unittest.main()
