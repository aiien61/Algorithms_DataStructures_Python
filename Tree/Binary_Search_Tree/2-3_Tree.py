
class Node:
    def __init__(self, key: int):
        self.keys = [key]
        self.parent = None
        self.left = None
        self.right = None
        self._middle = None


    @property
    def middle(self):
        if self._middle:
            return self._middle
        return None    


    @middle.setter
    def middle(self, node: object):
        if self.is_single_key():
            return None
        self._middle = node
        return None


    @property
    def depth(self):
        node = self
        depth = 1
        while node.parent:
            depth += 1
            node = node.parent
        return depth


    def search(self, key: int) -> object:
        if self is None:
            return None

        if key in self.keys:
            return self
        elif key < self.get_first_key():
            return self.left.search(key)
        elif key > self.get_last_key():
            return self.right.search(key)
        else:
            return self.middle.search(key)
        

    def get_first_key(self):
        return self.keys[0]


    def get_last_key(self):
        return self.keys[-1]


    def get_middle_key(self):
        return self.keys[1]


    def is_single_key(self) -> bool:
        return True if len(self.keys) == 1 else False
    

    def is_double_keys(self) -> bool:
        return True if len(self.keys) == 2 else False


    def is_triple_keys(self):
        return True if len(self.keys) == 3 else False


    def is_fully_grown(self) -> bool:
        """Return True if children of all direction exist, otherwise, False"""
        has_left = True if self.left is not None else False
        has_right = True if self.right is not None else False
        if self.is_single_key():
            # 1 key
            return True if has_left and has_right else False
        else:
            # 2 keys
            has_middle = True if self.middle is not None else False
            return True if has_left and has_middle and has_right else False

    
    def is_leaf(self) -> bool:
        no_left = True if self.left is None else False
        no_right = True if self.right is None else False
        if self.is_single_key():
            # 1 key
            return True if no_left and no_right else False
        else:
            # 2 keys
            no_middle = True if self.middle is None else False
            return True if no_left and no_middle and no_right else False
        
    def insert_key(self, key_to_insert: int) -> object:
        """Insert new key and place it to the proper node, and return the inserted node."""
        if key_to_insert in self.keys:
            return self

        if key_to_insert < self.get_first_key():
            if self.left is not None:
                return self.left.insert_key(key_to_insert)
        elif key_to_insert > self.get_last_key():
            if self.right is not None:
                return self.right.insert_key(key_to_insert)
        else:
            if self.middle is not None:
                return self.middle.insert_key(key_to_insert)
        self.keys.append(key_to_insert)
        self.keys.sort()
        return self


"""
Goal: 
1. all terminal nodes are at the same level
2. all non-terminal nodes have fully grown (i.e. all the left and right are not empty)
"""
class BST_23Tree:
    inorder_array = []

    def __init__(self):
        self.root = None

    def insert(self, key: int) -> Node:
        """Insert new key into 23-tree and return new root node."""
        if self.root is None:
            self.root = Node(key)
            return None

        node_to_merge = self.root.insert_key(key)
        new_root = self.split_and_merge(node_to_merge)

        return new_root
    
    def split_and_merge(self, node: Node):
        """
        Split the triple-key node, and return the new root after merging new generated node into its
        parent node.
        """
        if not node.is_triple_keys():
            root = node
            while root.parent:
                root = root.parent
            return root

        node = self.split(node)
        if node.parent:
            new_parent_node = self.merge(node, node.parent)
            self.split_and_merge(new_parent_node)
        
        return None

    def split(self, node_to_split: Node) -> Node:
        """Return the split node"""
        left_child = node_to_split.left
        right_child = node_to_split.right
        middle_child = node_to_split.middle

        new_node = Node(node_to_split.get_middle_key())
        new_node.left = Node(node_to_split.get_first_key())
        new_node.right = Node(node_to_split.get_last_key())

        parent_node = node_to_split.parent
        if new_node.get_first_key() < parent_node.get_first_key():
            parent_node.left = new_node
        elif new_node.get_first_key() > parent_node.get_last_key():
            parent_node.right = new_node
        else:
            parent_node.middle = new_node

        new_node.parent = parent_node

    def merge(self, node: Node, parent: Node):
        pass

    def inorder(self, node):
        if node is None:
            return None

        self.inorder(node.left)
        self.inorder_array.extend(node.keys)
        if node.is_double_keys():
            self.inorder(node.middle)
        self.inorder(node.right)
        return None

    def is_balanced(self) -> bool:
        node = self.root
        if node is None:
            return True
        
        leaves = []
        leaves = self._collect_leafnodes(node, leaves)
        depth = None
        for leafnode in leaves:
            if not depth:
                depth = leafnode.depth
            if depth != leafnode.depth:
                return False
        return True


    def _collect_leafnodes(self, node: Node, leafnodes: list) -> list:
        if node.is_leaf():
            leafnodes.append(node)
            return leafnodes
        
        leafnodes = node._collect_leafnodes(node.left, leafnodes)
        if node.is_double_keys():
            leafnodes = node._collect_leafnodes(node.middle, leafnodes)
        leafnodes = node._collect_leafnodes(node.right, leafnodes)
        return leafnodes
        
    
if __name__ == "__main__":
    pass
            
