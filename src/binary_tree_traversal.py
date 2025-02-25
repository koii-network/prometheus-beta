class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        val (Any): The value stored in the node
        left (TreeNode, optional): Left child node, defaults to None
        right (TreeNode, optional): Right child node, defaults to None
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_traversals(root):
    """
    Perform recursive binary tree traversals (pre-order, in-order, post-order).
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        dict: A dictionary containing lists of node values for each traversal type
        - 'pre_order': Nodes visited in pre-order (root, left, right)
        - 'in_order': Nodes visited in-order (left, root, right)
        - 'post_order': Nodes visited in post-order (left, right, root)
    
    Edge cases:
        - Returns empty lists for None/empty tree
    """
    # Handle empty tree case
    if root is None:
        return {
            'pre_order': [],
            'in_order': [],
            'post_order': []
        }
    
    # Lists to store traversal results
    pre_order_list = []
    in_order_list = []
    post_order_list = []
    
    # Pre-order traversal helper
    def pre_order(node):
        if node:
            pre_order_list.append(node.val)
            pre_order(node.left)
            pre_order(node.right)
    
    # In-order traversal helper
    def in_order(node):
        if node:
            in_order(node.left)
            in_order_list.append(node.val)
            in_order(node.right)
    
    # Post-order traversal helper
    def post_order(node):
        if node:
            post_order(node.left)
            post_order(node.right)
            post_order_list.append(node.val)
    
    # Perform traversals
    pre_order(root)
    in_order(root)
    post_order(root)
    
    # Return dictionary of traversals
    return {
        'pre_order': pre_order_list,
        'in_order': in_order_list,
        'post_order': post_order_list
    }