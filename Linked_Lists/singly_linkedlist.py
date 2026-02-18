from dataclasses import dataclass
from typing import Self, Optional

@dataclass
class Node:
    value: int
    _next_node: Optional[Self] = None
    
    @property
    def next_node(self) -> Optional[Self]:
        return self._next_node
    
    @next_node.setter
    def next_node(self, value: Self) -> None:
        self._next_node = value
        return None

@dataclass
class LinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    _length: int = 0

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next_node

    def __str__(self):
        return " -> ".join([f'{node.value}' for node in self])

    @property
    def length(self) -> int:
        return self._length
    
    def to_list(self) -> list[int]:
        return [node.value for node in self]

    def append(self, value: int) -> bool:
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

        self._length += 1
        return True
    
    def prepend(self, value: int) -> bool:
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head = node
        
        self._length += 1
        return True
    
    def pop(self) -> Optional[Node]:
        if self._length == 0:
            return None
        
        prev = self.head
        temp = self.head
        while temp.next_node:
            prev = temp
            temp = temp.next_node
        
        self.tail = prev
        self.tail.next_node = None
        self._length -= 1
        if self._length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self) -> Optional[Node]:
        if not self.head:
            return None
        
        temp = self.head
        self.head = self.head.next_node
        temp.next_node = None

        self._length -= 1
        if self._length == 0:
            self.tail = None
        
        return temp
    
    def get_node(self, index: int) -> Optional[Node]:
        if index < 0 or self._length <= index:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next_node
        return temp
    
    def set_node(self, index: int, value: int) -> bool:
        node = self.get_node(index)
        if node is None:
            return False

        node.value = value
        return True
    
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or self._length < index:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self._length:
            return self.append(value)
        
        node = Node(value)
        
        temp = self.get_node(index - 1)
        node.next_node = temp.next_node
        temp.next_node = node
        self._length += 1
        return True
    
    def remove(self, index: int) -> Optional[Node]:
        if index < 0 or self._length <= index:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self._length - 1:
            return self.pop()
        
        prev = self.get_node(index - 1)
        temp = prev.next_node
        prev.next_node = temp.next_node
        temp.next_node = None
        self._length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head

        before = None
        after = temp.next_node

        for _ in range(self._length):
            after = temp.next_node
            temp.next_node = before
            before = temp
            temp = after
        
        return None  

def main():
    llist = LinkedList()
    llist.append(3)
    llist.append(5)
    llist.append(10)
    print(llist)

    llist.pop()
    print(llist)
    llist.pop()
    print(llist)
    llist.pop()
    print(llist)
    print(llist.pop())

    llist.prepend(10)
    print(llist)
    llist.prepend(3)
    print(llist)

    print(llist.pop_first())
    print(llist)
    print(llist.pop_first())
    print(llist)
    print(llist.pop_first())

    print(llist.get_node(1))
    llist.append(10)
    llist.append(5)
    llist.append(3)
    print(llist)
    print(llist.get_node(0))
    print(llist.get_node(2))
    llist.set_node(2, 20)
    print(llist)

    llist.insert(1, 30)
    print(llist)

    print(llist.remove(100))
    print(llist.remove(0))
    print(llist)
    print(llist.remove(1))
    print(llist)

    llist.append(100)
    print(llist)
    llist.reverse()
    print(llist)

    print(llist.to_list())


if __name__ == "__main__":
    main()
