import unittest

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    def test_simple_checkout(self):
        self.assertEqual(checkout_solution.checkout('A'), 50)

    def test_multiple_items_checkout(self):
        self.assertEqual(checkout_solution.checkout('BADABA'), 190)

    def test_no_items_checkout(self):
        self.assertEqual(checkout_solution.checkout(''), 0)

    def test_invalid_item_checkout(self):
        self.assertEqual(checkout_solution.checkout('AAAZ'), -1)

    def test_discount_checkout(self):
        self.assertEqual(checkout_solution.checkout('BB'), 45)

    def test_no_discount_checkout(self):
        self.assertEqual(checkout_solution.checkout('ABCD'), 115)

    def test_normal_price_after_discount(self):
        self.assertEqual(checkout_solution.checkout('AAAA'), 180)
        self.assertEqual(checkout_solution.checkout('BBB'), 75)


if __name__ == '__main__':
    unittest.main()
