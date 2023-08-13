import unittest
from main import Solution, SinglyLinkedList, Node


class Test(unittest.TestCase):

    def test_delete_midnode(self):
        sol = Solution()
        linkedlist = SinglyLinkedList([1, 2, 3, 4, 5])
        node = Node(6)
        linkedlist.append(node)
        linkedlist.append_multiple([7, 8, 9])
        sol.delete_midnode(node, linkedlist)
        self.assertFalse(sol.has_node(Node(6), linkedlist))

if __name__ == "__main__":
    unittest.main()
