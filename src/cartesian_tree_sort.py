class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian tree from an input array.
    
    A Cartesian tree is a binary tree where:
    1. The tree is heap-ordered (parent is the maximum)
    2. An in-order traversal gives the original array
    
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
        # Create new node
        node = Node(value)
        
        # Find the last node that is smaller than current node
        while stack and stack[-1].value < value:
            node.left = stack.pop()
        
        # If stack is not empty, current node becomes right child
        if stack:
            stack[-1].right = node
        
        # Push current node to stack
        stack.append(node)
    
    # The last node in stack is the root
    return stack[0]

def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted array in ascending order
    """
    if not arr:
        return []
    
    # Build Cartesian tree
    root = build_cartesian_tree(arr)
    
    # In-order traversal to get sorted array
    def in_order_traversal(node, result):
        if not node:
            return
        
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)
    
    sorted_arr = []
    in_order_traversal(root, sorted_arr)
    return sorted_arr