from dataclasses import dataclass
from typing import Self, Optional

@dataclass
class Node:
    value: int
    prev_node: Optional[Self] = None
    next_node: Optional[Self] = None

@dataclass
class DoublyLinkedList:
    head: Optional[Node] = None
    tail: Optional[Node] = None
    length: int = 0

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next_node
    
    def __str__(self):
        return " <-> ".join([str(node.value) for node in self])
    
    def to_list(self) -> list[int]:
        return [node.value for node in self]
    
    def append(self, value: int) -> bool:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            temp.prev_node = None

        self.length -= 1
        return temp
    
    def prepend(self, value: int) -> bool:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head = new_node
        
        self.length += 1
        return True
    
    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
            temp.next_node = None

        self.length -= 1
        return temp
    
    def get_node(self, index: int) -> Optional[Node]:
        if index < 0 or self.length <= index:
            return None
        
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next_node
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev_node

        return temp

    def set_node(self, index: int, value: int) -> bool:
        temp = self.get_node(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: int) -> bool:
        if index < 0 or self.length < index:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        after = self.get_node(index)
        before = after.prev_node

        new_node.prev_node = before
        new_node.next_node = after

        before.next_node = new_node
        after.prev_node = new_node
        
        self.length += 1
        return True

    def remove(self, index: int) -> Optional[Node]:
        if index < 0 or self.length <= index:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get_node(index)

        temp.next_node.prev_node = temp.prev_node
        temp.prev_node.next_node = temp.next_node

        temp.prev_node = None
        temp.next_node = None

        self.length -= 1
        return temp

def main():
    dllist = DoublyLinkedList()
    dllist.append(10)
    dllist.append(20)
    print(dllist)

    print(dllist.pop())
    print(dllist)
    print(dllist.pop())
    print(dllist)

    dllist.prepend(10)
    print(dllist)
    dllist.prepend(20)
    print(dllist)
    dllist.prepend(15)
    print(dllist)

    print(dllist.pop_first())
    print(dllist)

    print(dllist.get_node(10))
    print(dllist.get_node(1))
    print(dllist.get_node(0))

    dllist.set_node(0, 30)
    print(dllist)

    dllist.insert(1, 20)
    print(dllist)

    print(dllist.remove(1))
    print(dllist)

if __name__ == "__main__":
    main()
