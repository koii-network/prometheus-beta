class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_traversals(root):
    """
    Perform pre-order, in-order, and post-order traversals on a binary tree.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        dict: A dictionary containing lists of node values for each traversal type
    """
    # Handle empty tree case
    if root is None:
        return {
            'pre_order': [],
            'in_order': [],
            'post_order': []
        }
    
    def pre_order_traversal(node):
        """Helper function for pre-order traversal (root -> left -> right)"""
        if node is None:
            return []
        return [node.val] + pre_order_traversal(node.left) + pre_order_traversal(node.right)
    
    def in_order_traversal(node):
        """Helper function for in-order traversal (left -> root -> right)"""
        if node is None:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    def post_order_traversal(node):
        """Helper function for post-order traversal (left -> right -> root)"""
        if node is None:
            return []
        return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.val]
    
    return {
        'pre_order': pre_order_traversal(root),
        'in_order': in_order_traversal(root),
        'post_order': post_order_traversal(root)
    }