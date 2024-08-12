"""Scheduling Minimise Lateness

Given a single resource is available starting at the same timepoint and a set of requests. 
Each request requires a contiguous interval of length and has different deadline

Goal: Schedule all requests without overlapping so as to minimise the maximum lateness.
"""
from typing import List, Union
from pprint import pprint
from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Request:
    i: int
    length: int
    due: int
    start: int = None
    finish: int = None


class Stack(ABC):
    @abstractmethod
    def push(self) -> None: raise NotImplementedError

    @abstractmethod
    def pop(self) -> object: raise NotImplementedError

    @abstractmethod
    def peek(self) -> object: raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool: raise NotImplementedError

    @abstractmethod
    def __repr__(self) -> str: raise NotImplementedError


class ResourceStack(Stack):
    def __init__(self):
        self.stack_list: List[Request] = []
        self.height: int = 0

    def push(self, element: Request) -> None:
        self.stack_list.append(element)
        self.height += 1
        return None
    
    def pop(self) -> Union[Request, None]:
        if self.height == 0:
            return None
        self.height -= 1
        return self.stack_list.pop(-1)
    
    def peek(self) -> Union[Request, None]:
        if self.height == 0:
            return None
        return self.stack_list[-1]
    
    def is_empty(self) -> bool:
        return True if self.height == 0 else False
    
    def __repr__(self) -> str:
        return str([element for element in self.stack_list])
    
    def __iter__(self):
        for element in self.stack_list:
            yield element

# Fabricating simulated requests
length: List[int] = [3, 2, 1, 4, 3, 2]
due: List[int] = [6, 8, 9, 9, 14, 15]
requests: List[tuple] = [Request(i+1, length[i], due[i]) for i in range(6)]

# Make a resource instance
resource = ResourceStack()

# Greedy Rule
# Earliest Due First: Process request in ascending order of deadlines

# O(NlogN)
# Step 1: Sorting requests in ascending order of deadlines
requests = sorted(requests, key=lambda r: r.due)
pprint(requests)

# O(N)
# Step 2: Loop all requests
for request in requests:
    # Step 3: Assign the current request to the resource from the start time being finish time of 
    # the previous assigned request to the finish time being the sum of the start time and the length
    # of the current request
    request.start = 0 if resource.is_empty() else resource.peek().finish
    request.finish = request.start + request.length
    resource.push(request)

pprint(resource)

# Maximum Lateness
# O(N)
max_lateness: int = 0
for request in resource:
    lateness = request.finish - request.due
    if lateness < 0:
        continue
    if lateness > max_lateness:
        max_lateness = lateness

print(f"max_lateness: {max_lateness}")
