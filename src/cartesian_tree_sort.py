class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian tree from the input array.
    
    A Cartesian tree is a binary tree where:
    1. The tree is heap-ordered (parent is always smaller/larger than children)
    2. An in-order traversal yields the original array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the Cartesian tree
    """
    if not arr:
        return None
    
    # Stack to maintain the tree structure
    stack = []
    
    for val in arr:
        # Create a new node for current value
        curr = Node(val)
        
        # Find the last node in the stack that is smaller
        while stack and stack[-1].value > val:
            # Current node becomes the right child of the last smaller node
            last = stack.pop()
            curr.left = last
        
        # If stack is not empty, current node becomes right child of top of stack
        if stack:
            stack[-1].right = curr
        
        # Push current node to stack
        stack.append(curr)
    
    # The last node in the stack is the root
    return stack[0]

def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Cartesian tree sort works by:
    1. Constructing a Cartesian tree from the input array
    2. Performing an in-order traversal to get sorted output
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted array in ascending order
    """
    if not arr:
        return []
    
    # Build Cartesian tree
    root = build_cartesian_tree(arr)
    
    # Perform in-order traversal to sort
    def in_order_traversal(node):
        if not node:
            return []
        
        return (in_order_traversal(node.left) + 
                [node.value] + 
                in_order_traversal(node.right))
    
    return in_order_traversal(root)