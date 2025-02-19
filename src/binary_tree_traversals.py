class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(root):
    """
    Perform in-order traversal of a binary tree (left -> root -> right)
    
    Args:
        root (Node): Root of the binary tree or subtree
    
    Returns:
        list: List of node values in in-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.extend(in_order_traversal(root.left))
    result.append(root.value)
    result.extend(in_order_traversal(root.right))
    
    return result

def pre_order_traversal(root):
    """
    Perform pre-order traversal of a binary tree (root -> left -> right)
    
    Args:
        root (Node): Root of the binary tree or subtree
    
    Returns:
        list: List of node values in pre-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.append(root.value)
    result.extend(pre_order_traversal(root.left))
    result.extend(pre_order_traversal(root.right))
    
    return result

def post_order_traversal(root):
    """
    Perform post-order traversal of a binary tree (left -> right -> root)
    
    Args:
        root (Node): Root of the binary tree or subtree
    
    Returns:
        list: List of node values in post-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.extend(post_order_traversal(root.left))
    result.extend(post_order_traversal(root.right))
    result.append(root.value)
    
    return result