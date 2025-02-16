class TreeNode:
    def __init__(self, value):
        """
        Initialize a tree node with a value and left/right child references.
        
        :param value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement tree sort algorithm to sort a list of comparable elements.
    
    Tree sort works by:
    1. Creating a binary search tree from the input array
    2. Performing an in-order traversal to retrieve elements in sorted order
    
    :param arr: List of comparable elements to be sorted
    :return: Sorted list of elements
    :raises TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Create the root of the binary search tree
    root = None
    
    # Insert each element into the binary search tree
    for item in arr:
        root = insert_node(root, item)
    
    # Create a list to store sorted elements
    sorted_list = []
    
    # Perform in-order traversal to collect sorted elements
    def in_order_traversal(node):
        if node:
            in_order_traversal(node.left)
            sorted_list.append(node.value)
            in_order_traversal(node.right)
    
    in_order_traversal(root)
    
    return sorted_list

def insert_node(root, value):
    """
    Insert a value into the binary search tree.
    
    :param root: Root of the current subtree
    :param value: Value to be inserted
    :return: Root of the modified subtree
    """
    # If the tree is empty, create a new node
    if root is None:
        return TreeNode(value)
    
    # Recursively insert into left or right subtree
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    
    return root