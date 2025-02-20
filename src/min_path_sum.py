class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root):
    """
    Find the minimum path sum from root to any leaf in a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        int: The minimum path sum, or float('inf') if the tree is empty
    """
    # Handle empty tree case
    if not root:
        return float('inf')
    
    # If it's a leaf node, return its value
    if not root.left and not root.right:
        return root.val
    
    # Initialize minimum path sum with a large value
    min_sum = float('inf')
    
    # Recursively check left subtree
    if root.left:
        left_min = min_path_sum(root.left)
        min_sum = min(min_sum, root.val + left_min)
    
    # Recursively check right subtree
    if root.right:
        right_min = min_path_sum(root.right)
        min_sum = min(min_sum, root.val + right_min)
    
    return min_sum