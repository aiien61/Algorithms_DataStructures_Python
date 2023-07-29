import unittest
import main

class Test(unittest.TestCase):
    data_T = [('abcd'), ('s4fad'), ('')]
    data_F = [('23ds2'), ('hb 627jh=j ()')]


    def test_has_unique_chars_by_set(self):
        # true check
        for test_string in self.data_T:
            actual = main.has_unique_chars_by_set(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.data_F:
            actual = main.has_unique_chars_by_set(test_string)
            self.assertFalse(actual)


    def test_has_unique_chars_by_array(self):
        # true check
        for test_string in self.data_T:
            actual = main.has_unique_chars_by_array(test_string)
            self.assertTrue(actual)
        
        # false check
        for test_string in self.data_F:
            actual = main.has_unique_chars_by_array(test_string)
            self.assertFalse(actual)

    def test_has_unique_chars_by_hash(self):
        # true check
        for test_string in self.data_T:
            actual = main.has_unique_chars_by_hash(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.data_F:
            actual = main.has_unique_chars_by_hash(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
