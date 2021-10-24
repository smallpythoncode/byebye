import unittest as ut

from main import roll_d20


class TestInputFunctions(ut.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def testRollD20ReturnsNumberInRange(self):
        self.assertIn(roll_d20(), list(range(1, 21)))


if __name__ == "__main__":
    ut.main()
