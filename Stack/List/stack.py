from typing import List

class Node:

    def __init__(self, value: int):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, array: List[int]=None):
        self.node_top = None
        if array:
            for i in range(len(array)):
                self.push(array[i])
    
    def push(self, value: int) -> None:
        node = Node(value)
        if not self.node_top:
            self.node_top = node
        else:
            node.next = self.node_top
            self.node_top = node
        return None
    
    def pop(self) -> int:
        if not self.node_top:
            return None
        
        node = self.node_top
        self.node_top = node.next
        node.next = None
        return node.value
    
    def __repr__(self):
        stack = []
        node = self.node_top
        while node:
            self.prepend(stack, node.value)
            node = node.next

        return f"stack({stack})"
    
    @classmethod
    def prepend(self, array: list, value: int) -> None:
        array.insert(0, value)
        return None

    
if __name__ == "__main__":
    numbers = list(range(1, 6))
    mystack = Stack()
    print(mystack)

    for n in numbers:
        mystack.push(n)
    print(mystack)

    # push
    mystack.push(6)
    print(mystack)

    # pop
    for _ in range(5):
        mystack.pop()
    print(mystack)

    # get last one
    bottom = mystack.pop()
    print(bottom)
    print(mystack)

    # pop from empty stack
    mystack.pop()
    print(mystack)

                


        


