class TreeNode:
    """
    Represents a node in a binary tree.
    
    Attributes:
        value (int): The value stored in the node.
        left (TreeNode, optional): Left child node. Defaults to None.
        right (TreeNode, optional): Right child node. Defaults to None.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs_ascending_order(root):
    """
    Perform a depth-first search on a binary tree and return node values in ascending order.
    
    Args:
        root (TreeNode): The root node of the binary tree.
    
    Returns:
        list: A list of node values in ascending order.
    
    Raises:
        TypeError: If the input is not a TreeNode or None.
    """
    # Handle edge cases
    if root is None:
        return []
    
    # Validate input type
    if not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # Use in-order traversal (left-root-right) to get ascending order
    result = []
    
    def _dfs_helper(node):
        """
        Recursive helper function to perform in-order traversal.
        
        Args:
            node (TreeNode): Current node being processed.
        """
        if node is None:
            return
        
        # Traverse left subtree first
        _dfs_helper(node.left)
        
        # Add current node's value
        result.append(node.value)
        
        # Traverse right subtree
        _dfs_helper(node.right)
    
    # Start the traversal
    _dfs_helper(root)
    
    return result