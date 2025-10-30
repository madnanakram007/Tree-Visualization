class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, key):
            self.value = key
            self.left = None
            self.right = None

    def insert(self, root, key):
        if root is None:
            return self.Node(key)
        else:
            if key < root.value:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def build_tree(self, values):
        """
        Build a complete tree from a list of values.
        """
        for value in values:
            self.root = self.insert(self.root, value)

    def traverse_tree(self, root):
        """
        Traverse the tree and return a list representing the structure.
        """
        if root is None:
            return None
        return {
            "value": root.value,
            "left": self.traverse_tree(root.left),
            "right": self.traverse_tree(root.right),
        }

    def inorder(self, root):
        if root:
            return self.inorder(root.left) + [root.value] + self.inorder(root.right)
        return []
