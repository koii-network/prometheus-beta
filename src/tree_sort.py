class TreeNode:
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
    Implement tree sort algorithm to sort a list of comparable elements.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Create the root of the binary search tree
    root = None
    
    # Insert each element into the binary search tree
    for item in arr:
        root = insert_node(root, item)
    
    # Collect sorted elements via in-order traversal
    sorted_list = []
    in_order_traversal(root, sorted_list)
    
    return sorted_list

def insert_node(root, value):
    """
    Insert a value into the binary search tree.
    
    Args:
        root (TreeNode): The root of the current subtree
        value: The value to be inserted
    
    Returns:
        TreeNode: The root of the updated subtree
    """
    # If tree is empty, create a new root node
    if root is None:
        return TreeNode(value)
    
    # Compare and insert into left or right subtree
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
        node (TreeNode): Current node in the traversal
        result (list): List to store sorted elements
    """
    if node is not None:
        # Traverse left subtree
        in_order_traversal(node.left, result)
        
        # Process current node
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right, result)