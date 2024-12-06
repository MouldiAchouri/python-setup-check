import unittest

from src.MathRequests import MathRequest

class TestMathRequests(unittest.TestCase):

# setUp => est appelé automatiquement à chaque test.

    def setUp(self):
        self.ope1 = 5
        self.oper = "+"
        self.ope2 = 3
        self.mathRequests = MathRequest(self.ope1, self.oper, self.ope2)

    def test_get_ope1(self):
        self.assertEqual(self.mathRequests.get_ope1(), self.ope1)

    def test_get_oper(self):
        self.assertEqual(self.mathRequests.get_oper(), self.oper)

    def test_get_ope2(self):
        self.assertEqual(self.mathRequests.get_ope2(), self.ope2)

if __name__ == '__main__':
    unittest.main()


