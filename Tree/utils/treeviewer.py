import os
import subprocess
from queue import Queue
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    data: Any
    times: int = 1
    left: object = None
    right: object = None


def _dot_node(node: object) -> str:
    dot_node = '{} [label="{}", color={}, style=filled]\n'
    
    name = f"{node.data}: ({node.times})" if node.data is not None else "X"
    color = "orange" if node.data is not None else "white"
    return dot_node.format(id(node), name, color)


def _dot_path(node_from: object, node_to: object) -> str:
    dot_edge = f'{id(node_from)} -> {id(node_to)}\n'
    return dot_edge


def _node_balancing(new_node: object, node: object):
    if node.left:
        new_node.left = _copy(node.left)
        _node_balancing(new_node.left, node.left)
    else:
        new_node.left = Node(None)

    if node.right:
        new_node.right = _copy(node.right)
        _node_balancing(new_node.right, node.right)
    else:
        new_node.right = Node(None)
    
    return None


def _copy(node: object) -> object:
    node_copy = Node(node.data)
    node_copy.times = node.times
    return node_copy


def get_tree_graph(tree_root: object) -> str:
    new_root = _copy(tree_root)
    _node_balancing(new_root, tree_root)

    txt = ''
    queue = Queue(10)
    queue.put(new_root)
    
    while not queue.empty():
        node = queue.get()
        txt += _dot_node(node)
        
        if node.left:
            txt += _dot_path(node, node.left)
            queue.put(node.left)
        
        if node.right:
            txt += _dot_path(node, node.right)
            queue.put(node.right)
    return 'digraph g {\n' + txt + '}'


def plot_tree_graph(tree_root, to_file="tree_graph.png"):
    tree_graph = get_tree_graph(tree_root)

    filename, dot_extension = os.path.splitext(to_file)

    # where to store .dot file
    utils_path = os.path.dirname(os.path.abspath(__file__))
    tmp_dir = os.path.join(utils_path, '../images')
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    
    graph_path = os.path.join(tmp_dir, f'{filename}.dot')

    with open(graph_path, 'w') as f:
        f.write(tree_graph)
    
    # call dot command to visualise .dot file
    extension = dot_extension[1:]
    dot_path = os.path.relpath(graph_path, os.getcwd())
    file_path = os.path.join(os.path.dirname(dot_path), to_file)
    cmd = f'dot {dot_path} -T {extension} -o {file_path}'
    subprocess.run(cmd, shell=True)
