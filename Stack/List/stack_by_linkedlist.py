import unittest
from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None

class StackList:
    def __init__(self, value: Any=None):
        if value is None:
            self.top = None
            self.length = 0
        else:
            new_node = Node(value)
            self.top = new_node
            self.length = 1
    
    def push(self, value: Any) -> bool:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.length -= 1
        return temp
    
    def return_stack(self):
        result = []
        temp = self.top
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result
    

class Test(unittest.TestCase):
    def test_push(self):
        s = StackList(2)
        s.push(1)
        expected = [1, 2]
        actual = s.return_stack()
        self.assertEqual(actual, expected)

    def test_pop(self):
        s = StackList(4)
        s.push(3)
        s.push(2)
        s.push(1)

        popped = s.pop()
        expected = 1
        actual = popped.value
        self.assertEqual(actual, expected)

        expected = [2, 3, 4]
        actual = s.return_stack()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
