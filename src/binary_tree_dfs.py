class TreeNode:
    """
    A class representing a node in a binary tree.
    
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
    
    This function uses an in-order traversal (left-root-right) to collect 
    node values in ascending order for a binary search tree.
    
    Args:
        root (TreeNode): The root node of the binary tree.
    
    Returns:
        list: A list of node values in ascending order.
    
    Raises:
        TypeError: If the input is not a TreeNode or None.
    """
    # Input validation
    if root is not None and not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # Result list to store node values
    result = []
    
    def _in_order_traverse(node):
        """
        Recursive helper function to perform in-order traversal.
        
        Args:
            node (TreeNode): Current node being traversed.
        """
        # Base case: if node is None, return
        if node is None:
            return
        
        # Traverse left subtree first
        _in_order_traverse(node.left)
        
        # Add current node's value
        result.append(node.value)
        
        # Traverse right subtree
        _in_order_traverse(node.right)
    
    # Start the traversal from the root
    _in_order_traverse(root)
    
    return result