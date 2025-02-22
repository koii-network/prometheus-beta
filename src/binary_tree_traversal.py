class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_traversals(root):
    """
    Perform pre-order, in-order, and post-order traversals of a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        dict: A dictionary with three keys - 'preorder', 'inorder', and 'postorder',
              each containing a list of node values in the respective traversal order
    """
    # Pre-order, in-order, and post-order traversal results
    preorder = []
    inorder = []
    postorder = []
    
    def traverse(node):
        if not node:
            return
        
        # Pre-order: root -> left -> right
        preorder.append(node.val)
        
        # Recursive traversal of left subtree
        if node.left:
            traverse(node.left)
        
        # In-order: left -> root -> right
        inorder.append(node.val)
        
        # Recursive traversal of right subtree
        if node.right:
            traverse(node.right)
        
        # Post-order: left -> right -> root
        postorder.append(node.val)
    
    # Start the recursive traversal if root exists
    if root:
        traverse(root)
    
    return {
        'preorder': preorder,
        'inorder': inorder,
        'postorder': postorder
    }