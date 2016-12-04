import unittest
from two import ex1, ex2

class Test20160201(unittest.TestCase):
    def setUp(self):
        self.number_matrix = {(0,0):'1', (1,0):'2', (2,0):'3',
                (0,1): '4', (1,1): '5', (2,1): '6',
                (0,2): '7', (1,2): '8', (2,2): '9'}
        self.current_number = (1,1)

    def test_instructions_interpreted_correctly(self):
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.assertEqual(self.current_number, (1,0))
        self.assertEqual(self.number_matrix[self.current_number], '2')

        self.current_number = (1,1)
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], '1')
        self.current_number = ex1.next_number("R", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("R", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], '9')
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("R", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], '8')

class Test20160202(unittest.TestCase):
    def setUp(self):
        self.current_number = (0,2)
        self.number_matrix = {(2,0):'1',
        (1,1): '2', (2,1): '3', (3,1): '4',
        (0,2): '5', (1,2): '6', (2,2): '7', (3,2): '8', (4,2): '9',
        (1,3): 'A', (2,3): 'B', (3,3): 'C',
        (2,4): 'D'}

    def test_instructions_interpreted_correctly(self):
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], '5')
        self.current_number = ex1.next_number("R", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("R", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], 'D')
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("R", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("L", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], 'B')
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("U", self.current_number, self.number_matrix)
        self.current_number = ex1.next_number("D", self.current_number, self.number_matrix)
        self.assertEqual(self.number_matrix[self.current_number], '3')
if __name__ == "__main__":
    unittest.main()
