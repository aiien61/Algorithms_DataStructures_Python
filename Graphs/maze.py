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
    map: Dict[tuple, tuple] = bfs_search(MAZE, (0, 2))
    print(path_to((2, 2), (0, 2), map))
