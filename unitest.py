import unittest

from my_math import iseven

class TestEval(unittest.TestCase):

    def test_even_value(self):

        self.assertTrue(iseven(4))
    
    def test_odd_value(self):
        self.assertFalse(iseven(5))



if __name__ =="__main__":
    unittest.main()