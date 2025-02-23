class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_ascending_order(root):
    """
    Perform a depth-first search on a binary tree and return node values in ascending order.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        list: A list of node values in ascending order
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Use an in-order traversal to get ascending order
    def in_order_traversal(node):
        if not node:
            return []
        
        # Recursively traverse left subtree
        left_values = in_order_traversal(node.left)
        
        # Add current node value
        current_value = [node.val]
        
        # Recursively traverse right subtree
        right_values = in_order_traversal(node.right)
        
        # Combine the results
        return left_values + current_value + right_values
    
    # Return the sorted list of values
    return in_order_traversal(root)