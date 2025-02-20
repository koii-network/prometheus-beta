class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert_node(root, key):
    """
    Insert a new node with the given key into the binary search tree
    
    Args:
        root (TreeNode): The root of the binary search tree
        key (int): The key to be inserted
    
    Returns:
        TreeNode: The root of the modified binary search tree
    """
    # If the tree is empty, create a new node as the root
    if root is None:
        return TreeNode(key)
    
    # If the key is less than the current node's key, insert in the left subtree
    if key < root.key:
        root.left = insert_node(root.left, key)
    
    # If the key is greater than the current node's key, insert in the right subtree
    elif key > root.key:
        root.right = insert_node(root.right, key)
    
    # If the key is equal to the current node's key, we do not insert duplicates
    
    return root

def inorder_traversal(root):
    """
    Perform an inorder traversal of the binary search tree
    
    Args:
        root (TreeNode): The root of the binary search tree
    
    Returns:
        list: A list of keys in sorted order
    """
    result = []
    
    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append(node.key)
            _inorder(node.right)
    
    _inorder(root)
    return result