class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def prepend(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        return None

    def append(self, data):
        self.size += 1
        new_node = Node(data)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        new_node.prev = node
        return None

    def insert(self, data, position):
        self.size += 1

        if position == 0:
            self.prepend(data)
            return None

        new_node = Node(data)
        current = self.head
        prev = None
        count = 0
        while current is not None:
            if count == position:
                break
            prev = current
            current = current.next
            count += 1

        if current is not None:
            new_node.next = current
            current.prev = new_node
        prev.next = new_node
        new_node.prev = prev
        return None

    def remove(self, data):
        if not self.head:
            return None

        current = self.head
        while current is not None:
            if current.data == data:
                break
            current = current.next

        if current is None:
            return None

        self.size -= 1
        if current.prev is None:
            current.next.prev = None
            self.head = current.next
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        return None

    def __repr__(self):
        string = []
        node = self.head
        while node is not None:
            string.append(node.data)
            node = node.next
        return str(string)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value


if __name__ == "__main__":
    doubly_linked_list = LinkedList()
    print(doubly_linked_list)
    print(doubly_linked_list.size)
    print()

    doubly_linked_list.prepend(0)
    print(doubly_linked_list)
    print(doubly_linked_list.size)
    print()

    data = [20, 30, 50, 10, 90, 80, 70]
    for _ in range(len(data)):
        doubly_linked_list.append(data.pop())
        print(doubly_linked_list)
        print(doubly_linked_list.size)
        print()

    doubly_linked_list.insert(60, 3)
    print(doubly_linked_list)
    print(doubly_linked_list.size)
    print()

    doubly_linked_list.remove(90)
    print(doubly_linked_list)
    print(doubly_linked_list.size)
    print()

    doubly_linked_list.insert(60, 10)
    print(doubly_linked_list)
    print(doubly_linked_list.size)
    print()
