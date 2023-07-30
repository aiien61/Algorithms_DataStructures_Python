import unittest
import main

class Test(unittest.TestCase):

    fruits = ['apple', 'pineapple', "banana", "orange", "grape", "pear"]

    def test_array_stringbuilder(self):
        expected = main.join_words(self.fruits)
        actual = main.join_words_by_array_stringbuilder(self.fruits)
        self.assertEqual(actual, expected)

    def test_linkedlist_stringbuilder(self):
        expected = main.join_words(self.fruits)
        actual = main.join_words_by_linkedlist_stringbuilder(self.fruits)
        self.assertEqual(actual, expected)        


if __name__ == "__main__":
    unittest.main()
