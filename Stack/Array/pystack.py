import numpy as np
from typing import Any


class PyStack:
    def __init__(self, size: int):
        self._stack = np.full(size, np.nan)
        self._size = size
        self._i_top = -1

    def __repr__(self):
        return f"stack({self._stack[:self._i_top+1]})"

    @property
    def size(self) -> int:
        return self._size
    
    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size
        self._stack = self._expand_stack(new_size)
        return None
    
    def _expand_stack(self, new_size: int) -> np.ndarray:
        new_stack = np.full(self._size, np.nan)
        new_stack[:self._i_top+1] = self._stack[:self._i_top+1]
        return new_stack
    
    def push(self, element) -> None:
        if self.is_full():
            raise StackException("PyStackOverflow")
        else:
            self._i_top += 1
            self._stack[self._i_top] = element
            return None

    def pop(self) -> Any:
        if self.is_empty():
            raise StackException("PyStackOverflow")
        else:
            element = self._stack[-1]
            self._stack[self._i_top] = np.nan
            self._i_top -= 1
            return element
    
    @property
    def top(self):
        return self._stack[self._i_top]
    
    def is_full(self) -> bool:
        return True if (self._i_top + 1 == self._size) else False
    
    def is_empty(self) -> bool:
        return True if self._i_top < 0 else False
    
    def empty(self) -> None:
        """Clear stack"""
        self._stack = np.full(self._size, np.nan)
        self._i_top = -1
        return None


class StackException(Exception):
    def __init__(self, message):
        self.message = message
    
    def __repr__(self):
        return self.message
    

if __name__ == "__main__":
    numbers = list(range(1, 6))
    mystack = PyStack(len(numbers))
    print(mystack)

    for n in numbers:
        mystack.push(n)
    print(mystack)

    # push
    try:
        mystack.push(6)
    except StackException as e:
        print(str(e))

    # pop
    for _ in range(5):
        mystack.pop()
    print(mystack)

    # pop from empty stack
    try:
        mystack.pop()
    except StackException as e:
        print(str(e))