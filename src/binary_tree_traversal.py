class Node:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        value: The value stored in the node
        left: Left child node (can be None)
        right: Right child node (can be None)
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def traverse_in_order(root):
    """
    Perform an in-order depth-first traversal of the binary tree.
    
    In-order traversal visits nodes in the order: left -> root -> right
    
    Args:
        root (Node): The root node of the binary tree
    
    Returns:
        list: A list of node values in in-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.extend(traverse_in_order(root.left))
    result.append(root.value)
    result.extend(traverse_in_order(root.right))
    
    return result

def traverse_pre_order(root):
    """
    Perform a pre-order depth-first traversal of the binary tree.
    
    Pre-order traversal visits nodes in the order: root -> left -> right
    
    Args:
        root (Node): The root node of the binary tree
    
    Returns:
        list: A list of node values in pre-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.append(root.value)
    result.extend(traverse_pre_order(root.left))
    result.extend(traverse_pre_order(root.right))
    
    return result

def traverse_post_order(root):
    """
    Perform a post-order depth-first traversal of the binary tree.
    
    Post-order traversal visits nodes in the order: left -> right -> root
    
    Args:
        root (Node): The root node of the binary tree
    
    Returns:
        list: A list of node values in post-order traversal sequence
    """
    if root is None:
        return []
    
    result = []
    result.extend(traverse_post_order(root.left))
    result.extend(traverse_post_order(root.right))
    result.append(root.value)
    
    return result