import unittest
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    value: int
    prev: Optional['Node'] = None
    next: Optional['Node'] = None

class DoublyLinkedList:
    def __init__(self, value: Optional[int]=None):
        new_node = Node(value) if value is not None else None
        self.head = new_node
        self.tail = new_node
        self.length = 0 if new_node is None else 1

    def return_list(self) -> List[int]:
        result = []
        temp = self.head
        while temp:
            result.append(temp.value)
            temp = temp.next
        return result

    def print_list(self) -> None:
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        print(' -> '.join(result))

    
    def append(self, value: int) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node | None:
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp
    
    def prepend(self, value: int) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> Node | None:
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None
        if index < (self.length / 2):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index: int, value: int) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    
    def remove(self, index: int) -> Node | None:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

class Evaluate(unittest.TestCase):
    def test_append(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(llist.return_list(), [1, 2, 3])

        llist = DoublyLinkedList()
        llist.append(1)
        llist.append(2)
        llist.append(3)
        self.assertEqual(llist.return_list(), [1, 2, 3])

    def test_prepend(self):
        llist = DoublyLinkedList(1)
        llist.prepend(2)
        llist.prepend(3)
        self.assertEqual(llist.return_list(), [3, 2, 1])

        llist = DoublyLinkedList()
        llist.prepend(1)
        llist.prepend(2)
        llist.prepend(3)
        self.assertEqual(llist.return_list(), [3, 2, 1])

    def test_pop(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.pop()
        self.assertEqual(llist.return_list(), [1, 2])

        llist = DoublyLinkedList()
        actual = llist.pop()
        expected = None
        self.assertEqual(actual, expected)

    def test_pop_first(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.pop_first()
        self.assertEqual(llist.return_list(), [2, 3])

        llist = DoublyLinkedList()
        actual = llist.pop_first()
        expected = None
        self.assertEqual(actual, expected)

    def test_get(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        actual = llist.get(1).value
        expected = 2
        self.assertEqual(actual, expected)

        llist = DoublyLinkedList()
        actual = llist.get(0)
        expected = None
        self.assertEqual(actual, expected)
    
    def test_set_value(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.set_value(1, 4)
        self.assertEqual(llist.return_list(), [1, 4, 3])

        llist = DoublyLinkedList()
        llist.set_value(0, 1)
        self.assertEqual(llist.return_list(), [])

        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.set_value(10, 4)
        self.assertEqual(llist.return_list(), [1, 2, 3])

    def test_insert(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.insert(1, 4)
        self.assertEqual(llist.return_list(), [1, 4, 2, 3])

        llist = DoublyLinkedList()
        llist.insert(0, 1)
        self.assertEqual(llist.return_list(), [1])

        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.insert(3, 4)
        self.assertEqual(llist.return_list(), [1, 2, 3, 4])
        
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.insert(10, 4)
        self.assertEqual(llist.return_list(), [1, 2, 3])

    def test_remove(self):
        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.remove(1)
        self.assertEqual(llist.return_list(), [1, 3])

        llist = DoublyLinkedList()
        llist.remove(0)
        self.assertEqual(llist.return_list(), [])

        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.remove(2)
        self.assertEqual(llist.return_list(), [1, 2])

        llist = DoublyLinkedList(1)
        llist.append(2)
        llist.append(3)
        llist.remove(10)
        self.assertEqual(llist.return_list(), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
