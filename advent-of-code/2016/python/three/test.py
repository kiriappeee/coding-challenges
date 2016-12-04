#http://adventofcode.com/2016/day/3
import unittest
from three import ex1, ex2

class Test20160301(unittest.TestCase):
    def setUp(self):
        pass

    def test_triangle_can_be_identified_correctly(self):
        self.assertTrue(ex1.is_triangle([27,10,25]))
        self.assertFalse(ex1.is_triangle([25,5,10]))

class Test20160302(unittest.TestCase):
    def setUp(self):
        self.lines = [
                [101, 301, 501],
                [102, 302, 502],
                [103, 303, 503],
                [201, 401, 601],
                [202, 402, 602],
                [203, 403, 603]
                ]

    def test_lines_are_counted_by_columns(self):
        self.assertEqual(ex2.get_triangles_from_columns(self.lines), [[101,102,103], [201,202,203], [301,302,303], [401,402,403], [501,502,503],[601,602,603]])


if __name__ == "__main__":
    unittest.main()
