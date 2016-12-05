#adventofcode.com/2016/day/5

import unittest
from five import ex

class Test20160501(unittest.TestCase):
    def setUp(self):
        pass

    def test_first_hash_can_be_found(self):
        self.assertEqual(ex.find_next_hash_character('abc', 0), ('1', 3231929, '00000155f8105dff7f56ee10fa9b9abd'))
        self.assertEqual(ex.find_next_hash_character('abc', 3231930), ('8', 5017308, '000008f82c5b3924a1ecbebf60344e00'))

    def test_full_password_can_be_found(self):
        self.assertEqual(ex.find_password('abc'), '18f47a30')

class Test20160502(unittest.TestCase):
    def setUp(self):
        pass

    def test_both_hash_and_character_is_found(self):
        self.assertEqual(ex.find_next_hash_character_two('abc', 0), ('5', 1, 3231929))
        self.assertEqual(ex.find_next_hash_character_two('abc', 3231930), ('', None, 5017308))

    def test_full_password_can_be_found_for_second_door(self):
        self.assertEqual(ex.find_password_door_two('abc'), '05ace8e3')

if __name__ == "__main__":
    unittest.main()
