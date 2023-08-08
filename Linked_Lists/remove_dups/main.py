class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, data_list: list):
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


    def append_multiple(self, data_list: list):
        if self.head is None:
            self.head = Node(data_list.pop(0))

        current = self.head
        while current.next is not None:
            current = current.next
        for data in data_list:
            node = Node(data)
            current.next = node
            current = current.next
        return None


class Solution:
    def remove_dups_by_set(self, unsorted_singlylinkedlist) -> None:
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
        sol.remove_dups_by_set(mylist)
        print(f"manipulated mylist: {mylist.data}")
        actual = mylist.data
        if actual == expected:
            print("OK!\n")
