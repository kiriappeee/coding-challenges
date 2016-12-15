# http://adventofcode.com/2016/day/9
import unittest
from nine import ex

class Test20160901(unittest.TestCase):
    def test_string_with_single_marker_decompresses_correctly(self):
        self.assertEqual(ex.decompress_message("A(1x5)BC"), "ABBBBBC")
        self.assertEqual(ex.decompress_message("(3x3)XYZ"), "XYZXYZXYZ")

    def test_string_with_multiple_markers_decompresses_correctly(self):
        self.assertEqual(ex.decompress_message("A(2x2)BCD(2x2)EFG"), "ABCBCDEFEFG")
        self.assertEqual(ex.decompress_message("(6x1)(1x3)A"), "(1x3)A")
        self.assertEqual(ex.decompress_message("X(8x2)(3x3)ABCY"), "X(3x3)ABC(3x3)ABCY")

class Test20160902(unittest.TestCase):
    def test_message_decompressed_can_be_predicted(self):
        self.assertEqual(ex.find_decompress_length("(3x3)XYZ"), 9)
        self.assertEqual(ex.find_decompress_length("X(8x2)(3x3)ABCY"), len("XABCABCABCABCABCABCY"))
        self.assertEqual(ex.find_decompress_length("(27x12)(20x12)(13x14)(7x10)(1x12)A"), 241920)
        self.assertEqual(ex.find_decompress_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"), 445)
if __name__ == "__main__":
    unittest.main()
