import unittest
from two import ex1, ex2

class Test20160201(unittest.TestCase):
    def setUp(self):
        ex1.CURRENT_NUMBER = (1,1)

    def test_instructions_interpreted_correctly(self):
        ex1.next_number("U")
        self.assertEqual(ex1.CURRENT_NUMBER, (1,0))
        self.assertEqual(ex1.NUMBER_MATRIX[ex1.CURRENT_NUMBER], 2)

        ex1.CURRENT_NUMBER = (1,1)
        ex1.next_number("U")
        ex1.next_number("L")
        ex1.next_number("L")
        self.assertEqual(ex1.NUMBER_MATRIX[ex1.CURRENT_NUMBER], 1)
        ex1.next_number("R")
        ex1.next_number("R")
        ex1.next_number("D")
        ex1.next_number("D")
        ex1.next_number("D")
        self.assertEqual(ex1.NUMBER_MATRIX[ex1.CURRENT_NUMBER], 9)
        ex1.next_number("L")
        ex1.next_number("U")
        ex1.next_number("R")
        ex1.next_number("D")
        ex1.next_number("L")
        self.assertEqual(ex1.NUMBER_MATRIX[ex1.CURRENT_NUMBER], 8)

if __name__ == "__main__":
    unittest.main()
