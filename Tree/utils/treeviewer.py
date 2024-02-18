import os
import subprocess
import numpy as np
from queue import Queue
from dataclasses import dataclass
from typing import Any
from multimethod import multimethod


@dataclass
class Node:
    value: Any
    left: object = None
    right: object = None


def _dot_node(node: object, is_from_array: bool=False) -> str:
    dot_node = '{} [label="{}", color={}, style=filled]\n'
    
    if is_from_array:
        name = f"{node.value}" if not np.isnan(node.value) else "X"
        color = "orange" if not np.isnan(node.value) else "white"
    else:
        name = f"{node.value}" if node.value is not None else "X"
        color = "orange" if node.value is not None else "white"
    
    return dot_node.format(id(node), name, color)


def _dot_path(node_from: Any, node_to: Any) -> str:
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
    node_copy = Node(node.value)
    return node_copy


@multimethod
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


@multimethod
def get_tree_graph(tree_root_index: int, tree_array: np.ndarray) -> str:
    txt = ''
    nodes = [Node(value) for value in tree_array]
    queue = Queue(10)
    queue.put(tree_root_index)
    
    while not queue.empty():
        i = queue.get()
        txt += _dot_node(nodes[i], True)

        left_i = (i + 1) * 2 - 1
        if left_i >= tree_array.size:
            null_node = Node(np.nan)
            txt += _dot_node(null_node, True)
            txt += _dot_path(nodes[i], null_node)
        elif np.isnan(tree_array[left_i]):
            txt += _dot_node(nodes[left_i], True)
            txt += _dot_path(nodes[i], nodes[left_i])
        else:
            txt += _dot_path(nodes[i], nodes[left_i])
            queue.put(left_i)

        right_i = (i + 1) * 2 - 1 + 1
        if right_i >= tree_array.size:
            null_node = Node(np.nan)
            txt += _dot_node(null_node, True)
            txt += _dot_path(nodes[i], null_node)
        elif np.isnan(tree_array[right_i]):
            txt += _dot_node(nodes[right_i], True)
            txt += _dot_path(nodes[i], nodes[right_i])
        else:
            txt += _dot_path(nodes[i], nodes[right_i])
            queue.put(right_i)

    return 'digraph g {\n' + txt + '}'


@multimethod
def plot_dot_graph(tree_root_index: int, tree_array: np.ndarray):
    return get_tree_graph(tree_root_index, tree_array)


@multimethod
def plot_dot_graph(tree_root: object):
    return get_tree_graph(tree_root)


def plot_tree_graph(tree_structure: str, to_file="tree_graph.png", **kwargs):
    if tree_structure.lower() == 'array':
        tree_graph = get_tree_graph(kwargs.get("tree_root_index"), kwargs.get("tree_array")) 
    elif tree_structure.lower() == "list":
        tree_graph = get_tree_graph(kwargs.get("tree_root"))

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
