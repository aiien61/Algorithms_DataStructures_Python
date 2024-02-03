from typing import List


class Stack:
    def __init__(self, array: List[int]=None):
        self.stack = []
        self._i_top = None
        if array:
            for i in range(len(array)):
                self.stack.append(array[i])
            self._i_top = i

    def push(self, value: int) -> None:
        self.stack.append(value)        
        self._i_top = 0 if not self._i_top else self._i_top + 1
        return None
    
    def pop(self) -> (int, None):
        if not self.stack:
            return None
        
        self._i_top -= 1
        return self.stack.pop()
        
    @property
    def size(self):
        return self._i_top
    
    def __repr__(self):
        return f"stack({self.stack})"
    

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



