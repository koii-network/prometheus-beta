class TreeNode:
    def __init__(self, value):
        """
        Initialize a tree node with a value and left/right child references.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Perform tree sort on the input array.
    
    Tree sort works by:
    1. Creating a binary search tree from the input array
    2. Performing an in-order traversal to get sorted elements
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A sorted version of the input list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Create root of the binary search tree
    root = None
    
    # Insert all elements into the binary search tree
    for item in arr:
        root = insert_node(root, item)
    
    # Collect sorted elements via in-order traversal
    sorted_arr = []
    in_order_traversal(root, sorted_arr)
    
    return sorted_arr

def insert_node(root, value):
    """
    Insert a value into the binary search tree.
    
    Args:
        root (TreeNode): Root of the current subtree
        value: Value to be inserted
    
    Returns:
        TreeNode: Updated root of the subtree
    """
    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)
    
    # Recursive insertion based on BST property
    try:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    except TypeError:
        raise ValueError("List contains non-comparable elements")
    
    return root

def in_order_traversal(node, result):
    """
    Perform in-order traversal of the binary search tree.
    
    Args:
        node (TreeNode): Current node in traversal
        result (list): List to store sorted elements
    """
    if node is not None:
        # Traverse left subtree
        in_order_traversal(node.left, result)
        
        # Append current node's value
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right, result)