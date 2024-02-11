import os
import subprocess
from queue import Queue


def _dot_node(node: object) -> str:
    dot_node = '{} [label="{}", color=orange, style=filled]\n'
    
    name = f"{node.data}: ({node.times})"
    return dot_node.format(id(node), name)

def _dot_path(node_from: object, node_to: object) -> str:
    dot_edge = f'{id(node_from)} -> {id(node_to)}\n'
    return dot_edge

# TODO: add None node if not both right and left node are None, otherwise, no need to add None node
def get_tree_graph(tree_root: object) -> str:
    txt = ''
    queue = Queue(10)
    queue.put(tree_root)
    
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

    # store as .dot file
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
