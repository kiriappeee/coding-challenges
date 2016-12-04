#http://adventofcode.com/2016/day/3
import unittest
from three import ex1

class Test20160301(unittest.TestCase):
    def setUp(self):
        pass

    def test_triangle_can_be_identified_correctly(self):
        self.assertTrue(ex1.is_triangle([27,10,25]))
        self.assertFalse(ex1.is_triangle([25,5,10]))

if __name__ == "__main__":
    unittest.main()
