import unittest
from six import ex

class Test20160601(unittest.TestCase):
    def setUp(self):
        self.test_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split('\n')

    def test_common_character_per_column_is_found(self):
        self.assertEqual(ex.find_common_character_in_column(0, self.test_input), "e")
        self.assertEqual(ex.find_common_character_in_column(1, self.test_input), "a")
        self.assertEqual(ex.find_common_character_in_column(3, self.test_input), "t")

    def test_word_is_detected_from_input(self):
        self.assertEqual(ex.get_error_corrected_message(self.test_input), "easter")

class Test20160602(unittest.TestCase):
    def setUp(self):
        self.test_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""".split('\n')

    def test_leas_common_character_per_column_is_found(self):
        self.assertEqual(ex.find_common_character_in_column(0, self.test_input, least=True), "a")
        self.assertEqual(ex.find_common_character_in_column(1, self.test_input, least=True), "d")
        self.assertEqual(ex.find_common_character_in_column(3, self.test_input, least=True), "e")

    def test_word_is_detected_from_input(self):
        self.assertEqual(ex.get_error_corrected_message(self.test_input, decoding_method="LEAST"), "advent")
if __name__ == "__main__":
    unittest.main()
