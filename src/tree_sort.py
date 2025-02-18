class TreeNode:
    def __init__(self, value):
        """
        Create a tree node with a given value.
        
        :param value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement tree sort algorithm.
    
    Tree sort works by:
    1. Creating a binary search tree from the input array
    2. Performing an in-order traversal to get a sorted array
    
    :param arr: Input list to be sorted
    :return: Sorted list in ascending order
    :raises TypeError: If input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Create root of the tree with first element
    root = TreeNode(arr[0])
    
    # Insert rest of the elements
    for item in arr[1:]:
        insert_node(root, item)
    
    # Collect sorted elements
    sorted_list = []
    in_order_traversal(root, sorted_list)
    
    return sorted_list

def insert_node(node, value):
    """
    Insert a value into the binary search tree.
    
    :param node: Current node in the tree
    :param value: Value to be inserted
    """
    if value < node.value:
        if node.left is None:
            node.left = TreeNode(value)
        else:
            insert_node(node.left, value)
    else:
        if node.right is None:
            node.right = TreeNode(value)
        else:
            insert_node(node.right, value)

def in_order_traversal(node, result):
    """
    Perform in-order traversal to collect sorted elements.
    
    :param node: Current node in the tree
    :param result: List to store sorted elements
    """
    if node is not None:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)