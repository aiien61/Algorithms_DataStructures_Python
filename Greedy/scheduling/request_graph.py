"""Use adjacency list to connect all requests
"""
from enum import Enum
from typing import List
from pprint import pprint
from collections import namedtuple

Request = namedtuple('Request', ['i', 'start', 'finish'])
requests: List[tuple] = []

def add_request(i: int, start: int, finish: int) -> None:
    requests.append(Request(i=i, start=start, finish=finish))
    return None

add_request(i=1, start=0, finish=2)
add_request(i=2, start=0, finish=5)
add_request(i=3, start=0, finish=2)
add_request(i=4, start=3, finish=5)
add_request(i=5, start=3, finish=9)
add_request(i=6, start=7, finish=10)
add_request(i=7, start=7, finish=10)
add_request(i=8, start=9, finish=13)
add_request(i=9, start=11, finish=13)
add_request(i=10, start=11, finish=13)

class TimeStatus(Enum):
    START = 1
    FINISH = 2

times: List[tuple] = []
for request in requests:
    start: int = request.start
    finish: int = request.finish
    times.append((request.i, TimeStatus.START, start))
    times.append((request.i, TimeStatus.FINISH, finish))
times = sorted(times, key=lambda t: t[2])

adjacency_list: dict = {request.i: set() for request in requests}
depth: int = 0
overlapping_set: set = set()

for time in times:
    request_i: int = time[0]
    if time[1] == TimeStatus.FINISH:
        overlapping_set.remove(request_i)
        depth -= 1
    elif time[1] == TimeStatus.START:
        overlapping_set.add(request_i)
        depth += 1

    if depth <= 1:
        continue

    for i in overlapping_set:
        if i == request_i:
            continue
        adjacency_list[i].add(request_i)
        adjacency_list[request_i].add(i)
    
pprint(adjacency_list)