from typing import List

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:

    def __init__(self, values: List[int]=None):
        self.head = None
        self.tail = None
        if values:
            self._init_queue(values)
    
    def _init_queue(self, values: List[int]) -> None:
        i = 0
        self.head = Node(values[i])
        node = self.head
        i += 1

        for value in values[i:]:
            node.next = Node(value)
            node = node.next

        self.tail = node
        return None
    
    def push(self, value: int) -> None:
        if not self.tail:
            self._init_queue([value])
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return None
    
    def poll(self) -> int:
        if not self.tail:
            return None

        node = self.head
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return node.value
    
    def __repr__(self):
        queue_string = []
        node = self.head
        while node:
            queue_string.append(node.value)
            node = node.next
        return f"Queue({queue_string})"


if __name__ == "__main__":
    values = list(range(1, 6))
    queue = Queue(values)
    print(queue)  # 1,2,3,4,5

    queue.push(6)
    print(queue)  # 1,2,3,4,5,6

    while True:
        value = queue.poll()
        if value is None:
            break
    print(queue)  # []

    value = queue.poll()
    print(value)  # None
    print(queue)  # []

    for value in range(11, 16):
        queue.push(value)
    print(queue)  # 11,12,13,14,15

    for _ in range(4):
        queue.poll()
    print(queue)  # 15

    for value in range(6):
        queue.push(value)
    print(queue)  # 15,0,1,2,3,4,5

    for value in range(0, 80):
        queue.push(value+30)
    print(queue)
