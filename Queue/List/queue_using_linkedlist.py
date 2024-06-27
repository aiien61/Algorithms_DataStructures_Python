import unittest
from typing import Any, List

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class QueueList:
    def __init__(self, value: Any=None):
        if value is not None:
            new_node = Node(value)
            self.front = new_node
            self.rear = new_node
            self.length = 1
        else:
            self.front = None
            self.rear = None
            self.length = 0

    def return_queue(self) -> List[Any]:
        result = []
        temp = self.front
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result

    def enqueue(self, value: Any) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
        return True
    
    def dequeue(self) -> Node:
        if self.length == 0:
            return None
        temp = self.front
        if self.length == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            temp.next = None
        self.length -= 1
        return temp
    

class Test(unittest.TestCase):
    def test_enqueue(self):
        my_queue = QueueList(1)
        my_queue.enqueue(2)
        expected = [1, 2]
        actual = my_queue.return_queue()
        self.assertEqual(expected, actual)

        """
            EXPECTED OUTPUT:
            ----------------
            Queue before enqueue(2):
            1

            Queue after enqueue(2):
            1, 2
        """

    def test_dequeue(self):
        my_queue = QueueList(1)
        my_queue.enqueue(2)
        expected = 1
        actual = my_queue.dequeue().value
        self.assertEqual(expected, actual)

        expected = [2]
        actual = my_queue.return_queue()
        self.assertEqual(expected, actual)

        expected = 2
        actual = my_queue.dequeue().value
        self.assertEqual(expected, actual)

        expected = []
        actual = my_queue.return_queue()
        self.assertEqual(expected, actual)

        expected = None
        actual = my_queue.dequeue()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
