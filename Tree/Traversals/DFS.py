from dataclasses import dataclass
from typing import Iterable

class BinaryTreeList:
    def __init__(self, values: Iterable):
        self.root = None
        self._build_tree(values)

    
    @dataclass
    class Node:
        value: int
        left: object = None
        right: object = None

    def _build_tree(self, values: Iterable) -> None:
        if not values:
            return None
        
        nodes = [self.Node(value) for value in values]
        
        self.root = nodes[0]
        bound = len(nodes)
        for i, value in enumerate(nodes):
            i_left = (i + 1) * 2 - 1
            i_right = (i + 1) * 2
            if (i_left < bound) and (nodes[i_left].value is not None):
                nodes[i].left = nodes[i_left]
            if (i_right < bound) and (nodes[i_right].value is not None):
                nodes[i].right = nodes[i_right]
    
    def traverse(self, order_from="left", order_by="preorder") -> None:
        print(f"({order_by} by DFS {order_from})", end=" ")
        if self.root is None: 
            return None
        
        if order_by == "preorder":
            self.traverse_preorder(self.root, order_from)
        elif order_by == "inorder":
            self.traverse_inorder(self.root, order_from)
        elif order_by == "postorder":
            self.traverse_postorder(self.root, order_from)

        print()
        return None

    def traverse_preorder(self, node: object, order_from: str) -> None:
        if node is None :
            return None
        print(node.value, end=" ")

        if order_from == "left":
            self.traverse_preorder(node.left, order_from)
            self.traverse_preorder(node.right, order_from)
        elif order_from == "right":
            self.traverse_preorder(node.right, order_from)
            self.traverse_preorder(node.left, order_from)

        return None
    
    def traverse_inorder(self, node: object, order_from: str) -> None:
        if node is None:
            return None

        if order_from == "left":
            self.traverse_inorder(node.left, order_from)
            print(node.value, end=" ")
            self.traverse_inorder(node.right, order_from)
        elif order_from == "right":
            self.traverse_inorder(node.right, order_from)
            print(node.value, end=" ")
            self.traverse_inorder(node.left, order_from)

        return None
    
    def traverse_postorder(self, node: object, order_from: str) -> None:
        if node is None:
            return None

        if order_from == "left":
            self.traverse_postorder(node.left, order_from)
            self.traverse_postorder(node.right, order_from)
        elif order_from == "right":
            self.traverse_postorder(node.right, order_from)
            self.traverse_postorder(node.left, order_from)
        
        print(node.value, end=" ")

        return None


class BinaryTreeArray:
    def __init__(self, values: Iterable):
        self.values = values
        self.length = len(values)

    def traverse(self, order_from: str, order_by: str):
        print(f"({order_by} by DFS {order_from})", end=" ")
        if not self.values: return None
        i_root = 0
        
        if order_by == "preorder":
            self.traverse_preorder(i_root, order_from)
        elif order_by == "inorder":
            self.traverse_inorder(i_root, order_from)
        elif order_by == "postorder":
            self.traverse_postorder(i_root, order_from)
        
        print()
        return None
    
    def traverse_preorder(self, node_i: int, order_from: str) -> None:
        if node_i >= self.length:
            return None

        if self.values[node_i] is None:
            return None
        
        print(self.values[node_i], end=" ")
        i_left = (node_i + 1) * 2 - 1
        i_right = (node_i + 1) * 2

        if order_from == "left":
            self.traverse_preorder(i_left, order_from)
            self.traverse_preorder(i_right, order_from)
        elif order_from == "right":
            self.traverse_preorder(i_right, order_from)
            self.traverse_preorder(i_left, order_from)
        
        return None
    
    def traverse_inorder(self, node_i: int, order_from: str) -> None:
        if node_i >= self.length:
            return None

        if self.values[node_i] is None:
            return None

        i_left = (node_i + 1) * 2 - 1
        i_right = (node_i + 1) * 2

        if order_from == "left":
            self.traverse_inorder(i_left, order_from)
            print(self.values[node_i], end=" ")
            self.traverse_inorder(i_right, order_from)
        elif order_from == "right":
            self.traverse_inorder(i_right, order_from)
            print(self.values[node_i], end=" ")
            self.traverse_inorder(i_left, order_from)

        return None
    
    def traverse_postorder(self, node_i: int, order_from: str) -> None:
        if node_i >= self.length:
            return None

        if self.values[node_i] is None:
            return None

        i_left = (node_i + 1) * 2 - 1
        i_right = (node_i + 1) * 2

        if order_from == "left":
            self.traverse_postorder(i_left, order_from)
            self.traverse_postorder(i_right, order_from)
        elif order_from == "right":
            self.traverse_postorder(i_right, order_from)
            self.traverse_postorder(i_left, order_from)

        print(self.values[node_i], end=" ")

        return None


if __name__ == "__main__":
    values = [
                            5,
                 2,                     6,
            1,        4,         None,       7,
        None, None, 3, None, None, None, None, None
    ]

    print("--- traverse using linkedlist ---")

    list_tree = BinaryTreeList(values)
    list_tree.traverse(order_from="left", order_by="preorder")
    list_tree.traverse(order_from="left", order_by="inorder")
    list_tree.traverse(order_from="left", order_by="postorder")

    list_tree.traverse(order_from="right", order_by="preorder")
    list_tree.traverse(order_from="right", order_by="inorder")
    list_tree.traverse(order_from="right", order_by="postorder")

    print("--- traverse using array ---")

    array_tree = BinaryTreeArray(values)
    array_tree.traverse(order_from="left", order_by="preorder")
    array_tree.traverse(order_from="left", order_by="inorder")
    array_tree.traverse(order_from="left", order_by="postorder")

    array_tree.traverse(order_from="right", order_by="preorder")
    array_tree.traverse(order_from="right", order_by="inorder")
    array_tree.traverse(order_from="right", order_by="postorder")


                



