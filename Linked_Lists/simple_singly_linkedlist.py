import unittest
from typing import List

class Node:
    def __init__(self, value: int | float | str):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.value})'


class LinkedList:
    def __init__(self, value: int | float | str = None):
        node = Node(value) if value is not None else None
        self.head = node
        self.tail = node
        self.length = 1 if node else 0

    def print_list(self):
        nodelist = []
        node = self.head
        while node:
            nodelist.append(str(node))
            node = node.next
        print(' -> '.join(nodelist))

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: int | float | str):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        tmp = self.head
        pre = self.head
        while tmp.next:
            pre = tmp
            tmp = tmp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return tmp

    def prepend(self, value: int | float | str):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None

        tmp = self.head
        self.head = self.head.next
        tmp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        
        return tmp
    
    def get(self, index: int):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def set_value(self, index: int, value: int | float | str):
        tmp = self.get(index)
        if tmp:
            tmp.value = value
            return True
        return False

    def insert(self, index: int, value: int | float | str):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        tmp = self.get(index - 1)
        new_node.next = tmp.next
        tmp.next = new_node
        self.length += 1
        return True


    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        tmp = pre.next
        pre.next = tmp.next
        tmp.next = None
        self.length -= 1
        return tmp
        

    def reverse(self) -> bool:
        self.head, self.tail = self.tail, self.head
        before = None
        current = self.tail
        after = current.next
        while True:
            if current is None:
                break
            after = current.next
            current.next = before
            before = current
            current = after
        return True
    
    def to_list(self):
        tmp = self.head
        result = []
        while tmp:
            result.append(tmp.value)
            tmp = tmp.next
        return result


def make_linked_list(values: List[int | float | str]) -> LinkedList:
    linkedlist = LinkedList()
    for i in values:
        linkedlist.append(i)
    return linkedlist

    
class Verify(unittest.TestCase):
    def test_append(self):
        my_linked_list = LinkedList(1)
        my_linked_list.make_empty()
        my_linked_list.append(1)
        my_linked_list.append(2)
        
        samplelist = LinkedList(1)
        samplelist.append(2)
        expected = samplelist.to_list()
        actual = my_linked_list.to_list()
        self.assertEqual(expected, actual)


    def test_prepend(self):
        my_linked_list = LinkedList(2)
        my_linked_list.append(3)
        my_linked_list.prepend(1)
        actual = my_linked_list.to_list()
        expected = make_linked_list([1, 2, 3]).to_list()
        self.assertEqual(expected, actual)


    def test_pop_first(self):
        my_linked_list = LinkedList(2)
        my_linked_list.append(1)

        # (2) Items - Returns 2 Node
        actual = my_linked_list.pop_first().value
        expected = 2
        self.assertEqual(expected, actual)

        # (1) Item -  Returns 1 Node
        actual = my_linked_list.pop_first().value
        expected = 1
        self.assertEqual(expected, actual)
    
        # (0) Items - Returns None
        actual = my_linked_list.pop_first()
        expected = None
        self.assertEqual(expected, actual)

    
    def test_get(self):
        my_linked_list = LinkedList(0)
        my_linked_list.append(1)
        my_linked_list.append(2)
        my_linked_list.append(3)

        actual = my_linked_list.get(3).value
        expected = 3
        self.assertEqual(expected, actual)


    def test_set_value(self):
        my_linked_list = LinkedList(11)
        my_linked_list.append(3)
        my_linked_list.append(23)
        my_linked_list.append(7)

        my_linked_list.set_value(1, 4)

        actual = my_linked_list.to_list()
        expected = make_linked_list([11, 4, 23, 7]).to_list()
        self.assertEqual(expected, actual)


    def test_insert(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(3)

        my_linked_list.insert(1, 2)
        actual = my_linked_list.to_list()
        expected = make_linked_list([1, 2, 3]).to_list()
        self.assertEqual(expected, actual)


        my_linked_list.insert(0, 0)
        actual = my_linked_list.to_list()
        expected = make_linked_list([0, 1, 2, 3]).to_list()
        self.assertEqual(expected, actual)


        my_linked_list.insert(4, 4)
        actual = my_linked_list.to_list()
        expected = make_linked_list([0, 1, 2, 3, 4]).to_list()
        self.assertEqual(expected, actual)


    def test_remove(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)
        my_linked_list.append(5)

        my_linked_list.remove(2)
        expected = make_linked_list([1, 2, 4, 5]).to_list()
        actual = my_linked_list.to_list()
        self.assertEqual(expected, actual)

        my_linked_list.remove(0)
        expected = make_linked_list([2, 4, 5]).to_list()
        actual = my_linked_list.to_list()
        self.assertEqual(expected, actual)

        my_linked_list.remove(2)
        expected = make_linked_list([2, 4]).to_list()
        actual = my_linked_list.to_list()
        self.assertEqual(expected, actual)

    
    def test_reverse(self):
        my_linked_list = LinkedList(1)
        my_linked_list.append(2)
        my_linked_list.append(3)
        my_linked_list.append(4)

        my_linked_list.reverse()
        actual = my_linked_list.to_list()
        expected = make_linked_list([4, 3, 2, 1]).to_list()
        self.assertEqual(expected, actual)


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


def main():
    print("\n----- Test: Pop on linked list with one node -----\n")
    linked_list = LinkedList(1)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(1, popped_node.value, "Value of popped node:")
    check(None, linked_list.head, "Head of linked list:")
    check(None, linked_list.tail, "Tail of linked list:")
    check(0, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop on linked list with multiple nodes -----\n")
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(3, popped_node.value, "Value of popped node:")
    check(1, linked_list.head.value, "Head of linked list:")
    check(2, linked_list.tail.value, "Tail of linked list:")
    check(2, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop on empty linked list -----\n")
    linked_list = LinkedList(1)
    linked_list.head = None
    linked_list.tail = None
    linked_list.length = 0
    popped_node = linked_list.pop()
    check(None, popped_node, "Popped node from empty linked list:")
    check(None, linked_list.head, "Head of linked list:")
    check(None, linked_list.tail, "Tail of linked list:")
    check(0, linked_list.length, "Length of linked list:")

    print("\n----- Test: Pop all -----\n")
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.print_list()
    popped_node = linked_list.pop()
    check(2, popped_node.value, "Value of popped node (first pop):")
    check(1, linked_list.head.value, "Head of linked list (after first pop):")
    check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
    check(1, linked_list.length, "Length of linked list (after first pop):")
    popped_node = linked_list.pop()
    check(1, popped_node.value, "Value of popped node (second pop):")
    check(None, linked_list.head, "Head of linked list (after second pop):")
    check(None, linked_list.tail, "Tail of linked list (after second pop):")
    check(0, linked_list.length, "Length of linked list (after second pop):")
    popped_node = linked_list.pop()
    check(None, popped_node, "Popped node from empty linked list (third pop):")
    check(None, linked_list.head, "Head of linked list (after third pop):")
    check(None, linked_list.tail, "Tail of linked list (after third pop):")
    check(0, linked_list.length, "Length of linked list (after third pop):")


if __name__ == "__main__":
    unittest.main()
    
