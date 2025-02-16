class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian tree from the input array.
    
    A Cartesian tree is a binary tree where:
    1. The tree is a heap based on the input array values
    2. In-order traversal of the tree gives the original array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the Cartesian tree
    """
    if not arr:
        return None
    
    # Stack to maintain the tree structure
    stack = []
    
    for value in arr:
        # Create a new node for the current value
        node = Node(value)
        
        # Find the last node where the current node becomes the right child
        while stack and stack[-1].value > value:
            last = stack.pop()
        
        # If stack is not empty, update the tree structure
        if stack:
            stack[-1].right = node
        
        # If stack becomes empty, this is the root
        if not stack:
            root = node
        
        # Add current node to the stack
        stack.append(node)
    
    return root

def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Cartesian tree sort works by:
    1. Constructing a Cartesian tree from the input array
    2. Performing an in-order traversal to get the sorted array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted array
    """
    if not arr:
        return []
    
    # Build the Cartesian tree
    root = build_cartesian_tree(arr)
    
    # Collect sorted elements via in-order traversal
    sorted_arr = []
    
    def in_order_traversal(node):
        if not node:
            return
        
        in_order_traversal(node.left)
        sorted_arr.append(node.value)
        in_order_traversal(node.right)
    
    in_order_traversal(root)
    
    return sorted_arr