class TreeNode:
    def __init__(self, value):
        """
        Initialize a tree node with a given value.
        
        :param value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement the tree sort algorithm.
    
    Tree sort works by:
    1. Creating a binary search tree from the input array
    2. Performing an in-order traversal to get a sorted array
    
    :param arr: Input list to be sorted
    :return: Sorted list
    :raises TypeError: If input is not a list
    """
    # Check input type
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
    
    :param root: Root of the current subtree
    :param value: Value to be inserted
    :return: Updated root of the subtree
    """
    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)
    
    # Recursively insert into left or right subtree
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    
    return root

def in_order_traversal(node, result):
    """
    Perform in-order traversal to collect sorted elements.
    
    :param node: Current node in the traversal
    :param result: List to store sorted elements
    """
    if node is not None:
        # Traverse left subtree
        in_order_traversal(node.left, result)
        
        # Add current node's value
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right, result)