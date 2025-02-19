class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_traversals(root):
    """
    Perform recursive binary tree traversals.
    
    Args:
        root (TreeNode): Root of the binary tree
    
    Returns:
        dict: A dictionary containing lists of node values for three traversal types
    """
    if not root:
        return {
            'pre_order': [],
            'in_order': [], 
            'post_order': []
        }
    
    def pre_order_traversal(node):
        """Pre-order traversal: Root, Left, Right"""
        if not node:
            return []
        return [node.val] + pre_order_traversal(node.left) + pre_order_traversal(node.right)
    
    def in_order_traversal(node):
        """In-order traversal: Left, Root, Right"""
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    def post_order_traversal(node):
        """Post-order traversal: Left, Right, Root"""
        if not node:
            return []
        return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.val]
    
    return {
        'pre_order': pre_order_traversal(root),
        'in_order': in_order_traversal(root),
        'post_order': post_order_traversal(root)
    }