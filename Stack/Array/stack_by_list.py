from typing import List

class Stack:
    def __init__(self):
        self.stack_list: List[int] = []
        self.height = 0
    
    def push(self, value: int) -> None:
        self.stack_list.append(value)
        self.height += 1
        return None
    
    def pop(self) -> int:
        if self.height == 0:
            return None
        self.height -= 1
        return self.stack_list.pop(-1)
    
    def is_empty(self) -> bool:
        return True if self.height == 0 else False
    
    def peek(self) -> int:
        if self.height == 0:
            return None
        return self.stack_list[-1]