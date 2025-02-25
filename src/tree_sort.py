class TreeNode:
    """
    A class representing a node in a binary search tree for tree sort algorithm.
    
    Attributes:
        value: The value stored in the node
        left: Left child node (smaller values)
        right: Right child node (larger values)
    """
    def __init__(self, value):
        """
        Initialize a tree node with a given value.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement the tree sort algorithm to sort a list of comparable elements.
    
    Tree sort works by:
    1. Creating a binary search tree from the input list
    2. Performing an in-order traversal to extract sorted elements
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Create root of the binary search tree
    root = None
    
    # Insert each element into the binary search tree
    for item in arr:
        root = insert_node(root, item)
    
    # Collect sorted elements
    sorted_list = []
    in_order_traversal(root, sorted_list)
    
    return sorted_list

def insert_node(root, value):
    """
    Insert a value into the binary search tree.
    
    Args:
        root (TreeNode): The root of the current subtree
        value: The value to insert
    
    Returns:
        TreeNode: The root of the modified subtree
    """
    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)
    
    # Compare and insert to left or right subtree
    try:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    except TypeError:
        raise ValueError("List contains elements that cannot be compared")
    
    return root

def in_order_traversal(node, result):
    """
    Perform an in-order traversal to collect sorted elements.
    
    Args:
        node (TreeNode): The current node
        result (list): List to store sorted elements
    """
    if node is not None:
        # Traverse left subtree
        in_order_traversal(node.left, result)
        
        # Add current node's value
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right, result)