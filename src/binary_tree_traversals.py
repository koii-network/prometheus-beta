class Node:
    def __init__(self, value, left=None, right=None):
        """
        Initialize a binary tree node.
        
        :param value: The value stored in the node
        :param left: Left child node (default None)
        :param right: Right child node (default None)
        """
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Perform in-order traversal of a binary tree (left -> root -> right).
    
    :param root: Root node of the binary tree
    :return: List of node values in in-order traversal
    """
    if root is None:
        return []
    
    return (
        inorder_traversal(root.left) + 
        [root.value] + 
        inorder_traversal(root.right)
    )

def preorder_traversal(root):
    """
    Perform pre-order traversal of a binary tree (root -> left -> right).
    
    :param root: Root node of the binary tree
    :return: List of node values in pre-order traversal
    """
    if root is None:
        return []
    
    return (
        [root.value] + 
        preorder_traversal(root.left) + 
        preorder_traversal(root.right)
    )

def postorder_traversal(root):
    """
    Perform post-order traversal of a binary tree (left -> right -> root).
    
    :param root: Root node of the binary tree
    :return: List of node values in post-order traversal
    """
    if root is None:
        return []
    
    return (
        postorder_traversal(root.left) + 
        postorder_traversal(root.right) + 
        [root.value]
    )