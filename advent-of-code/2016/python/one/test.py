import unittest
from . import ex1, ex2

#format of test is <year><test number><sub test number>
class Test20160101(unittest.TestCase):
    def setUp(self):
        ex1.reset_position()

    def test_current_unit_starts_at_zero_zero(self):
        self.assertEqual(ex1.get_current_position(), (0,0))

    def test_current_unit_start_pointing_north(self):
        self.assertEqual(ex1.get_current_direction(), "NORTH")

    def test_instruction_can_be_issued(self):
        self.assertTrue(ex1.move("L5"))

    def test_direction_is_changed_when_moving(self):
        ex1.move("L5")
        self.assertEqual(ex1.get_current_direction(), "WEST")
        ex1.move("R5")
        self.assertEqual(ex1.get_current_direction(), "NORTH")
        ex1.move("R5")
        self.assertEqual(ex1.get_current_direction(), "EAST")
        ex1.move("R5")
        self.assertEqual(ex1.get_current_direction(), "SOUTH")
        ex1.move("L5")
        self.assertEqual(ex1.get_current_direction(), "EAST")

    def test_position_is_changed_when_moving(self):
        ex1.move("L5")
        self.assertEqual(ex1.get_current_position(), (-5,0))
        ex1.move("R2")
        self.assertEqual(ex1.get_current_position(), (-5,2))
        ex1.move("R2")
        self.assertEqual(ex1.get_current_position(), (-3,2))
        ex1.move("L6")
        self.assertEqual(ex1.get_current_position(), (-3,8))
        ex1.move("R2")
        self.assertEqual(ex1.get_current_position(), (-1,8))
        ex1.move("R15")
        self.assertEqual(ex1.get_current_position(), (-1,-7))

    def test_distance_from_start_is_calculated(self):
        ex1.move("R2")
        ex1.move("L3")
        self.assertEqual(ex1.get_distance_from_start(), 5)
        ex1.reset_position()
        ex1.move("R2")
        ex1.move("R2")
        ex1.move("R2")
        self.assertEqual(ex1.get_distance_from_start(), 2)
        ex1.reset_position()
        ex1.move("R2")
        ex1.move("R2")
        self.assertEqual(ex1.get_distance_from_start(), 4)
        ex1.reset_position()
        ex1.move("R5")
        ex1.move("L5")
        ex1.move("R5")
        ex1.move("R3")
        self.assertEqual(ex1.get_distance_from_start(), 12)

class Test20160102(unittest.TestCase):
    def setUp(self):
        ex1.reset_position()
        ex2.reset_position()

    def test_repeated_location_is_retrieved(self):
        move_list = ["R8", " R4", " R4", " R8\n" ]
        self.assertEqual(ex2.find_hq(move_list), (4,0))

    def test_locations_between_two_points_are_added(self):
        current_move = (0,1)
        self.assertEqual(ex2.get_positions_visited(current_move), [(0,1)])
        current_move = (0, 4)
        self.assertEqual(ex2.get_positions_visited(current_move), [(0,1),
            (0,2),
            (0,3),
            (0,4)])
        current_move = (0, -4)
        self.assertEqual(ex2.get_positions_visited(current_move), [(0,-1),
            (0,-2),
            (0,-3),
            (0,-4)])
        current_move = (1, -4)
        ex2.LAST_MOVE=(1, 3)
        self.assertEqual(ex2.get_positions_visited(current_move), [
            (1,2),
            (1,1),
            (1,0),
            (1,-1),
            (1,-2),
            (1,-3),
            (1,-4)])
        ex2.reset_position()
        current_move = (2,0)
        self.assertEqual(ex2.get_positions_visited(current_move), [
            (1,0),
            (2,0)])
        current_move = (-4,0)
        self.assertEqual(ex2.get_positions_visited(current_move), [
            (-1,0),
            (-2,0),
            (-3,0),
            (-4,0)])
        
if __name__ == "__main__":
    unittest.main()
