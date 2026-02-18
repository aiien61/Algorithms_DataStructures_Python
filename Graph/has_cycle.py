"""Detect whether or not a graph contains cycles using dfs."""
from typing import Dict

G: Dict[str, list] = {'a': ['b', 'c'],
                      'b': ['c'],
                      'c': []}

def has_cycle(directed_graph: Dict[str, list]) -> bool:
    marked: Dict[str, bool] = {}
    in_stack: Dict[str, bool] = {}

    def dfs(v):
        in_stack[v] = True
        marked[v] = True
        for w in directed_graph[v]:
            if w not in marked:
                if dfs(w):
                    return True
            else:
                if w in in_stack and in_stack[w]:
                    return True
        
        in_stack[v] = False
        return False
    
    for v in directed_graph:
        if v not in marked:
            if dfs(v):
                return True
    return False

if __name__ == "__main__":
    print(has_cycle(G))
