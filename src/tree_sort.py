class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implements the tree sort algorithm.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains elements that cannot be compared.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Build the binary search tree
    root = None
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
        root (TreeNode): The root of the current subtree.
        value: The value to be inserted.
    
    Returns:
        TreeNode: The root of the updated subtree.
    """
    if root is None:
        return TreeNode(value)
    
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
    Perform in-order traversal to collect sorted elements.
    
    Args:
        node (TreeNode): The current node.
        result (list): The list to store sorted elements.
    """
    if node:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)