class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian tree from the input array.
    
    A Cartesian tree is a binary tree where:
    1. The tree is defined recursively
    2. The tree satisfies the heap property (parent is the max element)
    3. The in-order traversal of the tree gives the original array
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the Cartesian tree
    """
    if not arr:
        return None
    
    # Find the maximum element and its index
    max_idx = arr.index(max(arr))
    
    # Create root node with the maximum element
    root = Node(arr[max_idx])
    
    # Recursively build left and right subtrees
    root.left = build_cartesian_tree(arr[:max_idx])
    root.right = build_cartesian_tree(arr[max_idx+1:])
    
    return root

def inorder_traversal(root):
    """
    Perform an in-order traversal of the Cartesian tree.
    
    Args:
        root (Node): Root of the Cartesian tree
    
    Returns:
        list: Sorted list obtained from in-order traversal
    """
    result = []
    
    def _traverse(node):
        if node is None:
            return
        
        _traverse(node.left)
        result.append(node.value)
        _traverse(node.right)
    
    _traverse(root)
    return result

def cartesian_tree_sort(arr):
    """
    Sort an input array using Cartesian tree sort algorithm.
    
    Args:
        arr (list): Input list to be sorted
    
    Returns:
        list: Sorted list
    """
    if not arr:
        return []
    
    # Build Cartesian tree
    tree_root = build_cartesian_tree(arr)
    
    # Perform in-order traversal to get sorted list
    return inorder_traversal(tree_root)