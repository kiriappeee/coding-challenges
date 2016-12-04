import unittest
from four import ex

class Test20160401(unittest.TestCase):
    def setUp(self):
        pass

    def test_string_is_broken_into_parts_correctly(self):
        self.assertEqual(ex.parse_encrypted_name("aaaaa-bbb-z-y-x-123[abxyz]"), ("aaaaa-bbb-z-y-x", 123, "abxyz"))

    def test_valid_checksum_can_be_calculated(self):
        self.assertTrue(ex.is_checksum_valid("aaaaa-bbb-z-y-x", "abxyz"))
        parsed_encryption = ex.parse_encrypted_name("a-b-c-d-e-f-g-h-987[abcde]")
        self.assertTrue(ex.is_checksum_valid(parsed_encryption[0], parsed_encryption[2]))
        parsed_encryption = ex.parse_encrypted_name("not-a-real-room-404[oarel]")
        self.assertTrue(ex.is_checksum_valid(parsed_encryption[0], parsed_encryption[2]))
        parsed_encryption = ex.parse_encrypted_name("totally-real-room-200[decoy]")
        self.assertFalse(ex.is_checksum_valid(parsed_encryption[0], parsed_encryption[2]))

if __name__ == "__main__":
    unittest.main()
