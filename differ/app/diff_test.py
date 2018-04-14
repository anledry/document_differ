import unittest
from diff_functions import get_diff_blocks

class TestDocumentDiff(unittest.TestCase):
    def test_equal_size_different_content_2_blocks(self):
        data1 = "HOLAMUNDO13578"
        data2 = "COLAMUNDO24678"

        diff_blocks = get_diff_blocks(data1, data2)

        self.assertTrue(len(diff_blocks) == 2, "Wrong diff blocks size.")
        self.assertTrue(diff_blocks[0] == 1, "Wrong comparison first block.")
        self.assertTrue(diff_blocks[9] == 3, "Wrong comparison second block.")

    def test_equal_size_equal_content(self):
        data1 = "HOLAMUNDO13578"
        data2 = "HOLAMUNDO13578"

        diff_blocks = get_diff_blocks(data1, data2)

        self.assertTrue(len(diff_blocks) == 0, "Wrong diff blocks size.")

    def test_different_size_value_error(self):
        data1 = "HOLAMUNDO13578"
        data2 = "HOLAMUNDO135783048239482"

        with self.assertRaises(ValueError):
            get_diff_blocks(data1, data2)

    def test_without_one_side_data_error(self):
        data1 = "HOLAMUNDO13578"
        data2 = ""

        with self.assertRaises(ValueError):
            get_diff_blocks(data1, data2)


if __name__ == '__main__':
    unittest.main()