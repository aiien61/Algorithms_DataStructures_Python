"""Interval Partitioning Problem (Interval Colouring)

Condition: multiple resources, and multiple requests

Goal: Partition these requests into a minimum number of compatible subsets, each corresponds to one resource
"""
from enum import Enum
from pprint import pprint
from typing import List, Deque, Tuple
from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections import namedtuple, deque

class TimeStatus(Enum):
    FINISH = 1
    START = 2


class RequestNode:
    def __init__(self, data: Tuple[int]):
        self.label: int = None
        self.data: Tuple[int] = data
        self.next: 'RequestNode' = None

    @property
    def start(self) -> int:
        return self.data.start
    
    @property
    def finish(self) -> int:
        return self.data.finish
    
    def __repr__(self) -> str:
        return f"Request(i={self.data.i}, label={self.label}, start={self.start}, finish={self.finish})"


class LinkedList:
    __index: int = 0

    @classmethod
    def _get_index(cls) -> int:
        index: int = cls.__index
        cls.__index += 1
        return index


class ResourceLinkedList(LinkedList):
    def __init__(self) -> None:
        self.label: int = self._get_index()
        self.head: RequestNode = None
        self.tail: RequestNode = None
        self.length: int = 0
    
    def append(self, node: RequestNode) -> None:
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1
            return None
        
        self.tail.next = node
        self.tail = node
        self.length += 1
        return None
    
    def is_empty(self) -> bool:
        return False if self.length else True
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        return str([str(node) for node in self])
        

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

resource_deque: Deque[object] = deque([ResourceLinkedList() for _ in range(max_depth)])


# Time complexity: O(NM), M is the max depth, list.append() costs amortised O(1)
for request in requests:
    request_node = RequestNode(data=request)
    while True:
        resource_linkedlist = resource_deque.popleft()
        if resource_linkedlist.is_empty():
            request_node.label = resource_linkedlist.label
            resource_linkedlist.append(request_node)
            resource_deque.append(resource_linkedlist)
            break

        if request_node.start < resource_linkedlist.tail.finish:
            resource_deque.append(resource_linkedlist)
            continue

        request_node.label = resource_linkedlist.label
        resource_linkedlist.append(request_node)
        resource_deque.append(resource_linkedlist)
        break

pprint(resource_deque)