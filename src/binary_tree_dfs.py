class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_ascending_order(root):
    """
    Perform a depth-first search on a binary tree and return node values in ascending order.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        list: A list of node values in ascending order
    """
    # If the root is None, return an empty list
    if not root:
        return []
    
    # Initialize result list to store values
    result = []
    
    # Helper function for in-order traversal (which gives ascending order for a BST)
    def in_order_traversal(node):
        # Recursively traverse left subtree
        if node.left:
            in_order_traversal(node.left)
        
        # Add current node's value
        result.append(node.value)
        
        # Recursively traverse right subtree
        if node.right:
            in_order_traversal(node.right)
    
    # Perform in-order traversal
    in_order_traversal(root)
    
    return result