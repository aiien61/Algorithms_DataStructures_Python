"""Interval Partitioning Problem (Interval Colouring)

Condition: multiple resources, and multiple requests

Goal: Partition these requests into a minimum number of compatible subsets, each corresponds to one resource
"""
from enum import Enum
from pprint import pprint
from typing import List, Deque
from abc import ABC, abstractmethod
from collections import namedtuple, deque

class TimeStatus(Enum):
    FINISH = 1
    START = 2

class Stack(ABC):
    __label: int = 0

    @classmethod
    def _get_label(cls) -> int:
        label: int = cls.__label
        cls.__label += 1
        return label

    @abstractmethod
    def push(self): raise NotImplementedError

    @abstractmethod
    def pop(self): raise NotImplementedError

    @abstractmethod
    def is_empty(self): raise NotImplementedError

    @abstractmethod
    def peek(self): raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str: raise NotImplementedError


class ResourceStack(Stack):
    def __init__(self):
        self.stack_list: List[object] = []
        self.height: int = 0
        self.label: int = self._get_label()

    def __repr__(self) -> str:
        return str([str(element) for element in self.stack_list])

    def push(self, element: object) -> None:
        self.stack_list.append(element)
        self.height += 1
        return None

    def pop(self) -> object:
        if self.height == 0:
            return None
        self.height -= 1
        return self.stack_list.pop(-1)

    def is_empty(self) -> bool:
        return True if self.height == 0 else False

    def peek(self) -> object:
        return self.stack_list[-1]
    
    def reverse(self) -> None:
        new_stack_list: List[object] = []
        for _ in range(self.height):
            new_stack_list.append(self.pop())
        self.stack_list = new_stack_list
        return None


Request = namedtuple('Request', ['i', 'start', 'finish'])
requests: List[tuple] = []

def add_request(i: int, start: int, finish: int) -> None:
    requests.append(Request(i=i, start=start, finish=finish))
    return None

add_request(i=0, start=3, finish=9)
add_request(i=1, start=11, finish=13)
add_request(i=2, start=0, finish=2)
add_request(i=3, start=3, finish=5)
add_request(i=4, start=7, finish=10)
add_request(i=5, start=0, finish=5)
add_request(i=6, start=9, finish=13)
add_request(i=7, start=0, finish=2)
add_request(i=8, start=7, finish=10)
add_request(i=9, start=11, finish=13)

# The depth of a set of requests: the maximum number that pass over any single point on the time-line
# i.e. the lower bound of the number of required resources
# Time complexity: O(N)
times: List[int] = []
for request in requests:
    start_time: int = request.start
    finish_time: int = request.finish
    times.append((request.i, TimeStatus.START, start_time))
    times.append((request.i, TimeStatus.FINISH, finish_time))

# Time complexity: O(NlogN)
times = sorted(times, key=lambda t: (t[2], t[1].value))  # in case two starts and one finish happen simultaneously

# Time complexity: O(N)
max_depth: int = 0
current_depth: int = 0
for t in times:
    if t[1] == TimeStatus.START:
        current_depth += 1
    elif t[1] == TimeStatus.FINISH:
        current_depth -= 1
    
    if current_depth > max_depth:
        max_depth = current_depth

print(max_depth)

# Sorting requests in ascending order of their starting times
# Time complexity: O(NlogN)
requests = sorted(requests, key=lambda r: r.start)
pprint(requests)

resource_deque: Deque[object] = deque([ResourceStack() for _ in range(max_depth)])


# TODO: use labelling to dispatch the requests
# Time complexity: O(NM), M is the max depth, list.append() costs amortised O(1)
for request in requests:
    while True:
        resource_stack = resource_deque.popleft()
        if resource_stack.is_empty():
            resource_stack.push(request)
            resource_deque.append(resource_stack)
            break

        if request.start < resource_stack.peek().finish:
            resource_deque.append(resource_stack)
            continue

        resource_stack.push(request)
        resource_deque.append(resource_stack)
        break

pprint(resource_deque)