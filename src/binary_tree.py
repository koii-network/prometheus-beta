class TreeNode:
    """
    Represents a node in a binary tree.
    
    Attributes:
        value (int): The value stored in the node
        left (TreeNode): Left child node
        right (TreeNode): Right child node
    """
    def __init__(self, value):
        """
        Initialize a tree node with a given value.
        
        Args:
            value (int): The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def dfs_ascending(root):
    """
    Perform a depth-first search (in-order traversal) 
    to return node values in ascending order.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        list: A list of node values in ascending order
    
    Raises:
        TypeError: If the input is not a TreeNode or None
    """
    # Check for invalid input
    if root is not None and not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # If tree is empty, return empty list
    if root is None:
        return []
    
    # In-order traversal (left-root-right) gives ascending order for BST
    result = []
    
    # Recursively traverse left subtree
    if root.left:
        result.extend(dfs_ascending(root.left))
    
    # Add current node's value
    result.append(root.value)
    
    # Recursively traverse right subtree
    if root.right:
        result.extend(dfs_ascending(root.right))
    
    return result