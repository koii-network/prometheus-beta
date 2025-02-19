class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse_tree(root):
    """
    Perform recursive binary tree traversals.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        dict: A dictionary containing pre-order, in-order, and post-order traversals
    """
    def pre_order_traversal(node):
        """Perform pre-order traversal (Root, Left, Right)"""
        if not node:
            return []
        return [node.value] + pre_order_traversal(node.left) + pre_order_traversal(node.right)
    
    def in_order_traversal(node):
        """Perform in-order traversal (Left, Root, Right)"""
        if not node:
            return []
        return in_order_traversal(node.left) + [node.value] + in_order_traversal(node.right)
    
    def post_order_traversal(node):
        """Perform post-order traversal (Left, Right, Root)"""
        if not node:
            return []
        return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.value]
    
    return {
        'pre_order': pre_order_traversal(root),
        'in_order': in_order_traversal(root),
        'post_order': post_order_traversal(root)
    }