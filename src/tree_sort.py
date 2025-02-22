class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement tree sort algorithm
    
    Args:
        arr (list): Input list of comparable elements to be sorted
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not arr:
        return []
    
    # Create root of binary search tree
    root = None
    
    # Insert all elements into the binary search tree
    for item in arr:
        root = insert_node(root, item)
    
    # Collect sorted elements through in-order traversal
    sorted_list = []
    in_order_traversal(root, sorted_list)
    
    return sorted_list

def insert_node(root, value):
    """
    Insert a value into the binary search tree
    
    Args:
        root (TreeNode): Root of the current subtree
        value: Value to be inserted
    
    Returns:
        TreeNode: Updated root of the subtree
    """
    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)
    
    # Recursively insert the value
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
    Perform in-order traversal to collect sorted elements
    
    Args:
        node (TreeNode): Current node in the traversal
        result (list): List to store sorted elements
    """
    if node is not None:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)