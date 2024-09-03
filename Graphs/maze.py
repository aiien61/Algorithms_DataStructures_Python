"""Find the path in maze from start to target point using dfs, bfs, and guided search approaches.
"""

import random
from dataclasses import dataclass
from typing import Dict, Tuple, List

MAZE: Dict[tuple, list] = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2)],
    (0, 2): [(0, 1), (0, 3), (1, 2)],
    (0, 3): [(0, 2), (0, 4), (1, 3)],
    (0, 4): [(0, 3), (1, 4)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(1, 0), (2, 1)],
    (1, 2): [(0, 2), (2, 2)],
    (1, 3): [(0, 3)],
    (1, 4): [(0, 4), (2, 4)],
    (2, 0): [(1, 0)],
    (2, 1): [(1, 1), (2, 2)],
    (2, 2): [(1, 2), (2, 1), (2, 3)],
    (2, 3): [(2, 2), (2, 4)],
    (2, 4): [(1, 4), (2, 3)]
}


@dataclass
class Node:
    value: Tuple[int] = None
    next: 'Node' = None
    priority: int = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self) -> bool:
        return self.top is None
    
    def push(self, value: Tuple[int]) -> bool:
        if self.is_empty():
            self.top = Node(value)
        else:
            node = Node(value)
            node.next = self.top
            self.top = node
        return True
    
    def pop(self) -> Tuple[int] | None:
        if self.is_empty():
            return None
        
        value: Tuple[int] = self.top.value
        self.top = self.top.next
        return value


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self) -> bool:
        return self.first is None
    
    def enqueue(self, value: Tuple[int]) -> bool:
        node = Node(value)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = self.last.next
        return True
    
    def dequeue(self) -> Tuple[int] | None:
        if self.is_empty():
            return None
        
        node: Node = self.first
        self.first = self.first.next
        node.next = None
        return node.value


class PriorityQueue:
    def __init__(self, size: int):
        self.size: int = size
        self.heap: List[Node] = [None] * size
        self.N = -1

    def is_empty(self) -> bool:
        return self.N < 0

    def is_full(self) -> bool:
        return (self.N + 1) == self.size

    def less(self, index1: int, index2: int) -> bool:
        if self.heap[index1] is None:
            return False
        if self.heap[index2] is None:
            return False
        return self.heap[index1].priority < self.heap[index2].priority

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return None

    def enqueue(self, value: Tuple[int], priority: int) -> bool:
        if self.is_full():
            return False
        
        self.N += 1
        self.heap[self.N] = Node(value=value, priority=priority)

        index: int = self.N
        while index > 0:
            if self.less(index // 2, index):
                self.swap(index // 2, index)
                index = index // 2
            else:
                break

        return True
    
    def dequeue(self) -> Tuple[int] | None:
        if self.is_empty():
            return None
        
        value: Tuple[int] = self.heap[0].value
        self.swap(0, self.N)
        self.heap[self.N] = None
        self.N -= 1
        index = 0
        while True :
            max_index: int = index
            if (index * 2 + 1) < self.size:
                if self.less(max_index, index * 2 + 1):
                    max_index = index * 2 + 1

            if (index * 2 + 2) < self.size:
                if self.less(max_index, index * 2 + 2):
                    max_index = index * 2 + 2

            if max_index == index:
                break
            index = max_index
        
        return value
            

def distance_between(from_: Tuple[int], target: Tuple[int]) -> int:
    return abs(target[0] - from_[0]) + abs(target[1] - from_[1])


def guided_search(G: Dict[tuple, list], src: Tuple[int], target: Tuple[int]) -> Dict[tuple, tuple]:
    marked: Dict[tuple, bool] = {}
    node_from: Dict[tuple, tuple] = {}

    unseen = PriorityQueue(len(G))
    marked[src] = True
    unseen.enqueue(src, distance_between(src, target))

    while not unseen.is_empty():
        v = unseen.dequeue()
        for w in G[v]:
            if w not in marked:
                marked[w] = True
                node_from[w] = v
                unseen.enqueue(w, distance_between(w, target))
    
    return node_from


def dfs_search(G: Dict[tuple, list], src: Tuple[int]) -> Dict[tuple, tuple]:
    marked: Dict[tuple, bool] = {}
    node_from: Dict[tuple, tuple] = {}

    unseen = Stack()
    marked[src] = True
    unseen.push(src)

    while not unseen.is_empty():
        v: Tuple[int] = unseen.pop()
        for w in random.sample(G[v], len(G[v])):
            if w not in marked:
                node_from[w] = v
                marked[w] = True
                unseen.push(w)

    return node_from


def bfs_search(G: Dict[tuple, list], src: Tuple[int]) -> Dict[tuple, tuple]:
    marked: Dict[tuple, bool] = {}
    node_from: Dict[tuple, tuple] = {}

    unseen = Queue()
    marked[src] = True
    unseen.enqueue(src)

    while not unseen.is_empty():
        v = unseen.dequeue()
        for w in random.sample(G[v], len(G[v])):
            if w not in marked:
                node_from[w] = v
                marked[w] = True
                unseen.enqueue(w)
    
    return node_from


def path_to(target: Tuple[int], src: Tuple[int], node_from: Dict[tuple, tuple]) -> List[int]:
    if target not in node_from:
        raise ValueError('Unreachable')
    
    path: List[int] = []
    v: Tuple[int] = target
    while v != src:
        path.append(v)
        v = node_from[v]
    
    path.append(src)
    return path[::-1]

if __name__ == '__main__':
    # map: Dict[tuple, tuple] = dfs_search(MAZE, (0, 2))
    # map: Dict[tuple, tuple] = bfs_search(MAZE, (0, 2))
    map: Dict[tuple, tuple] = guided_search(MAZE, (0, 2), (2, 2))
    print(path_to((2, 2), (0, 2), map))
