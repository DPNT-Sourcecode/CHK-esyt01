import unittest

from solutions.HLO import hello_solution


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello(), 'Hello, World!')
        self.assertEqual(hello_solution.hello(''), 'Hello, World!')
        self.assertEqual(hello_solution.hello('Craftsman'), 'Hello, Craftsman!')
        self.assertEqual(hello_solution.hello('Mr. X'), 'Hello, Mr. X!')


if __name__ == '__main__':
    unittest.main()
