import unittest
from eight import ex

class Test20160801(unittest.TestCase):
    def setUp(self):
        self.initialized_panel = ex.initialize_panel(col=7, row=3)

    def test_panel_can_be_initialized(self):
        self.assertEqual(len(self.initialized_panel), 3)
        self.assertEqual(len(self.initialized_panel[2]), 7)
        self.assertEqual(self.initialized_panel[2][0], 0)

    def test_instruction_can_be_parsed(self):
        self.assertEqual(ex.parse_instruction("rect 2x3"), {"instruction": "rect", "column": 2, "row": 3})
        self.assertEqual(ex.parse_instruction("rotate column x=1 by 1"), {"instruction": "down", "column": 1, "row": 1})
        self.assertEqual(ex.parse_instruction("rotate row y=0 by 4"), {"instruction": "right", "column": 4, "row": 0})

    def test_instruction_is_executed(self):
        panel = ex.execute_instruction("rect 3x2", self.initialized_panel)
        self.assertEqual(panel[0][0], 1)
        self.assertEqual(panel[0][1], 1)
        self.assertEqual(panel[0][2], 1)
        self.assertEqual(panel[1][0], 1)
        self.assertEqual(panel[1][1], 1)
        self.assertEqual(panel[1][2], 1)
        self.assertEqual(panel[2][0], 0)
        panel = ex.execute_instruction("rotate column x=1 by 1", panel)
        self.assertEqual(panel[0][1], 0)
        self.assertEqual(panel[1][1], 1)
        self.assertEqual(panel[2][1], 1)
        panel = ex.execute_instruction("rotate row y=0 by 4", panel)
        ex.print_panel(panel)
        self.assertEqual(panel[0][4], 1)
        self.assertEqual(panel[0][5], 0)
        self.assertEqual(panel[0][6], 1)
        self.assertEqual(panel[1][0], 1)
        self.assertEqual(panel[1][1], 1)
        self.assertEqual(panel[1][2], 1)
        self.assertEqual(panel[2][0], 0)
        self.assertEqual(panel[2][1], 1)
        self.assertEqual(panel[2][2], 0)
        panel = ex.execute_instruction("rotate column x=1 by 1", panel)

    def test_number_of_lights_on_can_be_counted(self):
        panel = ex.execute_instruction("rect 3x2", self.initialized_panel)
        self.assertEqual(ex.count_number_of_lights_on(panel), 6)
        panel = ex.execute_instruction("rotate column x=1 by 1", panel)
        panel = ex.execute_instruction("rotate row y=0 by 4", panel)
        panel = ex.execute_instruction("rotate column x=1 by 1", panel)
        self.assertEqual(ex.count_number_of_lights_on(panel), 6)
        panel = ex.execute_instruction("rect 3x2", self.initialized_panel)
        self.assertEqual(ex.count_number_of_lights_on(panel), 9)


class Test20160802(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
