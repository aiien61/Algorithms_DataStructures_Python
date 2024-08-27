import random
import unittest

from binary_search_tree import BSTreeArray as BST


class Test(unittest.TestCase):
    def test_insertion_when_only_root(self):
        bst = BST()
        bst.insert(10)

        expected: int = 10
        actual: int = bst.root
        self.assertEqual(expected, actual)

    def test_insertion_when_only_left_child(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)

        expected: int = 5
        actual: int = bst.array[bst.root_index * 2 + 1]
        self.assertEqual(expected, actual)

    def test_insertion_when_only_right_child(self):
        bst = BST()
        bst.insert(10)
        bst.insert(15)

        expected: int = 15
        actual: int = bst.array[bst.root_index * 2 + 2]
        self.assertEqual(expected, actual)

    def test_insertion_when_duplicate(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        expected: bool = False
        actual: bool = bst.insert(15)
        self.assertEqual(expected, actual)

    def test_contain_when_empty_tree(self):
        bst = BST()

        expected: bool = False
        actual: bool = bst.contains(10)
        self.assertEqual(expected, actual)

    def test_contain_when_only_root(self):
        bst = BST()
        bst.insert(10)

        expected: bool = True
        actual: bool = bst.contains(10)
        self.assertEqual(expected, actual)

    def test_contain_when_existing_left_child(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)

        expected: bool = True
        actual: bool = bst.contains(5)
        self.assertEqual(expected, actual)

    def test_contain_when_existing_right_child(self):
        bst = BST()
        bst.insert(10)
        bst.insert(15)

        expected: bool = True
        actual: bool = bst.contains(15)
        self.assertEqual(expected, actual)

    def test_contain_when_non_existing_element(self):
        bst = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        expected: bool = False
        actual: bool = bst.contains(25)
        self.assertEqual(expected, actual)

    def test_contain_when_large_input(self):
        random.seed(100)

        bst = BST()
        for _ in range(500):
            bst.insert(random.randint(1, 1000))
        bst.insert(500)
        for _ in range(500):
            bst.insert(random.randint(1, 1000))

        expected: bool = True
        actual: bool = bst.contains(500)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
