"""Use Greedy Algorithm to implement a simple interval-scheduling task.
Condition: single resource, multiple requests

Goal: Make compatible requests as more as possible fit into the single resource 
"""

import random
from pprint import pprint
from typing import List, Tuple
from collections import namedtuple


random.seed(100)

# Step 1: Initialise empty accepted requests set A, and undetermined requests set R
R: List[tuple] = []
A: List[tuple] = []

Request: Tuple[int] = namedtuple('Request', ['i', 'start', 'finish'])

for i in range(10):
    a, b = random.sample(range(24), 2)
    request = Request(i, a, b) if a < b else Request(i, b, a)
    R.append(request)

# Step 2: Sorting in the order of the finishing time of the requests
R = sorted(R, key=lambda r: (r.finish, r.start))
pprint(R)

# Step 3: While R is not empty, keep doing the following procedure
while R:
    # Step 4: Choosing the request with minimum finishing time, and remove it from set R
    # (pick the first one because R is already sorted in the ascending finishing time order)
    accepted_request: List[int] = R.pop(0)
    
    # Step 5: Set A add the accepted request
    A.append(accepted_request)

    # Step 6: Set R removes all conflicted requests which are not compatible with the accepted request in the set A.
    i: int = 0
    while i < len(R):
        request: tuple = R[i]
        if accepted_request.finish <= request.start:
            break
        R.pop(0)

pprint(A)
