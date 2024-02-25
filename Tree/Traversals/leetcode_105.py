"""Construct original binary tree from given pre-order, in-order, and post-order traversals.
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""

import os, sys
sys.path.append(os.pardir)
from utils.treeviewer import plot_tree_graph

import unittest
from dataclasses import dataclass
from typing import Iterable


@dataclass
class TreeNode:
    value: int
    left: object = None
    right: object = None


def build_tree(inorder: Iterable, **kwargs) -> TreeNode:
    if preorder := kwargs.get("preorder"):
        return buildtree_from_preorder(preorder, inorder)
    elif postorder := kwargs.get("postorder"):
        return buildtree_from_postorder(postorder, inorder)


def buildtree_from_preorder(preorder: Iterable, inorder: Iterable) -> TreeNode:
    if not preorder and not inorder:
        return None
    
    root = TreeNode(preorder[0])
    root_i = inorder.index(preorder[0])

    root.left = buildtree_from_preorder(preorder[1: root_i+1], inorder[: root_i])
    root.right = buildtree_from_preorder(preorder[root_i+1: ], inorder[root_i+1:])
    return root


def buildtree_from_postorder(postorder: Iterable, inorder: Iterable) -> TreeNode:
    if not postorder and not inorder:
        return None
    
    root = TreeNode(postorder[-1])
    root_i = inorder.index(postorder[-1])

    root.left = buildtree_from_postorder(postorder[: root_i], inorder[: root_i])
    root.right = buildtree_from_postorder(postorder[root_i: -1], inorder[root_i+1:])
    return root

def print_tree(root_node: TreeNode) -> list:
    result = []
    nulls = []
    queue = [root_node]
    while queue:
        node = queue.pop(0)

        if node:
            while nulls:
                result.append(nulls.pop(0))
            result.append(node.value)
            queue.append(node.left)
            queue.append(node.right)
        else:
            nulls.append(node)

    return result


class Test(unittest.TestCase):
    testcases = [
        {
            'traversals': {'preorder': [5, 2, 1, 4, 3, 6, 7], 'inorder': [1, 2, 3, 4, 5, 6, 7]},
            'expected': [5, 2, 6, 1, 4, None, 7, None, None, 3]
        },
        {
            'traversals': {'postorder': [1, 3, 4, 2, 7, 6, 5], 'inorder': [1, 2, 3, 4, 5, 6, 7]},
            'expected': [5, 2, 6, 1, 4, None, 7, None, None, 3]
        },
        {
            'traversals': {'postorder': [26, 6, 30, 17, 5, 9, 21], 'inorder': [26, 6, 30, 21, 9, 5, 17]},
            'expected': [21, 30, 9, 6, None, None, 5, 26, None, None, 17]
        },
        {
            'traversals': {'preorder': [10, 9, 7, 3, 6, 2, 8, 5, 4, 1], 'inorder': [3, 7, 9, 6, 2, 10, 5, 8, 4, 1]},
            'expected': [10, 9, 8, 7, 6, 5, 4, 3, None, None, 2, None, None, None, 1]
        },
        {
            'traversals': {'preorder': [-1], 'inorder': [-1]},
            'expected': [-1]
        },
        {
            'traversals': {'preorder': [3, 9, 20, 15, 7], 'inorder': [9, 3, 15, 20, 7]},
            'expected': [3, 9, 20, None, None, 15, 7]
        }

    ]
    def test_buildtree_from_traversals(self):
        for testcase in self.testcases:
            traversals = testcase.get('traversals')
            expected = testcase.get('expected')
            actual = print_tree(build_tree(**traversals))
            self.assertEqual(actual, expected)


        
if __name__ == "__main__":
    # preorder = [5, 2, 1, 4, 3, 6, 7]
    # postorder = [1, 3, 4, 2, 7, 6, 5]
    # inorder = [1, 2, 3, 4, 5, 6, 7]
    
    # root_node = build_tree(inorder=inorder, preorder=preorder)
    # plot_tree_graph(tree_structure="list", 
    #                 to_file="construct_tree_graph_from_preorder.png", tree_root=root_node)
    # tree = print_tree(root_node)
    # print(tree)

    # root_node = build_tree(inorder=inorder, postorder=postorder)
    # plot_tree_graph(tree_structure="list",
    #                 to_file="construct_tree_graph_from_postorder.png", tree_root=root_node)
    # tree = print_tree(root_node)
    # print(tree)

    # preorder = [-1]
    # inorder = [-1]
    # root_node = build_tree(inorder=inorder, preorder=preorder)
    # plot_tree_graph(tree_structure="list",
    #                 to_file="construct_tree_graph_from_preorder.png", tree_root=root_node)
    # tree = print_tree(root_node)
    # print(tree)
    
    # preorder = [10, 9, 7, 3, 6, 2, 8, 5, 4, 1]
    # inorder = [3, 7, 9, 6, 2, 10, 5, 8, 4, 1]
    # root_node = build_tree(preorder=preorder, inorder=inorder)
    # plot_tree_graph(tree_structure="list",
    #                 to_file="construct_tree_graph_from_preorder.png", tree_root=root_node)
    # tree = print_tree(root_node)
    # print(tree)


    # postorder = [26, 6, 30, 17, 5, 9, 21]
    # inorder = [26, 6, 30, 21, 9, 5, 17]
    # root_node = build_tree(inorder=inorder, postorder=postorder)
    # plot_tree_graph(tree_structure="list",
    #                 to_file="construct_tree_graph_from_postorder.png", tree_root=root_node)
    # tree = print_tree(root_node)
    # print(tree)

    unittest.main()
