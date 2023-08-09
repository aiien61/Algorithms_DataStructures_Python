from typing import List

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, data_list: List[int]):
        self.head = None
        if data_list:
            self.append_multiple(data_list)

    @property
    def data(self):
        node = self.head
        data_list = []
        while node is not None:
            data_list.append(node.data)
            node = node.next
        return data_list


    def append_multiple(self, data_list: List[int]):
        if not self.head:
            self.head = Node(data_list.pop(0))

        current = self.head
        while current.next is not None:
            current = current.next
        for data in data_list:
            current.next = Node(data)
            current = current.next
        return None


class Solution:
    # O(n)
    def remove_dups_by_set(self, unsorted_singlylinkedlist) -> None:
        if not unsorted_singlylinkedlist.head:
            return None

        node = unsorted_singlylinkedlist.head
        prev = None
        bags = set()
        while node is not None:
            if node.data in bags:
                prev.next = node.next
            else:
                bags.add(node.data)
                prev = node
            node = node.next
        return None
    
    # O(n)
    def remove_dups_by_hash(self, unsorted_singlylinkedlist) -> None:
        if not unsorted_singlylinkedlist.head:
            return None
        
        length = len(unsorted_singlylinkedlist.data)
        array = [False] * length
        node = unsorted_singlylinkedlist.head
        prev = None
        while node is not None:
            position = hash(node.data) % length
            if array[position]:
                prev.next = node.next
            else:
                array[position] = True
                prev = node
            node = node.next
        return None
    
    # O(n*n)
    # Follow up: solve this question without using additional memory
    def remove_dups_by_runner(self, unsorted_singlylinkedlist) -> None:
        if not unsorted_singlylinkedlist.head:
            return None

        current = unsorted_singlylinkedlist.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return None


if __name__ == "__main__":
    test_cases = (
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 5, 6, 7, 6, 5, 8, 1, 3], [0, 5, 6, 7, 8, 1, 3]),
        ([0, 0, 5, 6, 7, 6, 5, 8, 1, 8], [0, 5, 6, 7, 8, 1])
    )

    sol = Solution()
    for data, expected in test_cases:
        print(f"Test: {data}")
        mylist = SinglyLinkedList(data)
        print(f"original mylist: {mylist.data}")
        sol.remove_dups_by_runner(mylist)
        print(f"manipulated mylist: {mylist.data}")
        print(f"expected list: {expected}")
        actual = mylist.data
        if actual == expected:
            print("OK!\n")
        else:
            print("Fails!\n")
