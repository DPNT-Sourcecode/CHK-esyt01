import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    def test_simple_checkout(self):
        self.assertEqual(checkout_solution.checkout('A'), 50)


if __name__ == '__main__':
    unittest.main()
