class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_tree(root):
    """
    Perform tree traversals and return lists of node values.
    
    Args:
        root (TreeNode): The root of the binary tree.
    
    Returns:
        dict: A dictionary containing pre-order, in-order, and post-order traversals
    """
    if not root:
        return {
            'pre_order': [],
            'in_order': [],
            'post_order': []
        }
    
    def pre_order_traversal(node):
        """Recursive pre-order traversal (Root, Left, Right)"""
        if not node:
            return []
        return [node.val] + pre_order_traversal(node.left) + pre_order_traversal(node.right)
    
    def in_order_traversal(node):
        """Recursive in-order traversal (Left, Root, Right)"""
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
    
    def post_order_traversal(node):
        """Recursive post-order traversal (Left, Right, Root)"""
        if not node:
            return []
        return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.val]
    
    return {
        'pre_order': pre_order_traversal(root),
        'in_order': in_order_traversal(root),
        'post_order': post_order_traversal(root)
    }