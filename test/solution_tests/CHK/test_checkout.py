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

    def test_bonus_product_alter_total(self):
        self.assertEqual(checkout_solution.checkout('EE'), 80)
        self.assertEqual(checkout_solution.checkout('EEB'), 80)
        self.assertEqual(checkout_solution.checkout('EEEB'), 120)
        self.assertEqual(checkout_solution.checkout('EEEEBB'), 160)
        self.assertEqual(checkout_solution.checkout('BEBEEE'), 160)
        self.assertEqual(checkout_solution.checkout('ABCDEABCDE'), 280)

    def test_multiple_discounts_of_same_product(self):
        self.assertEqual(checkout_solution.checkout('AAAAA'), 200)
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('AAAAAAA'), 300)
        self.assertEqual(checkout_solution.checkout('AAAAAAAA'), 330)
        self.assertEqual(checkout_solution.checkout('AAAAAAAAAA'), 400)


if __name__ == '__main__':
    unittest.main()
