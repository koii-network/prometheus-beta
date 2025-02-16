class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr):
    """
    Build a Cartesian tree from an input array.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        Node: Root of the Cartesian tree
    """
    if not arr:
        return None
    
    # Create nodes for all elements
    nodes = [Node(x) for x in arr]
    
    # First node is always the root
    root = nodes[0]
    
    # Process the rest of the nodes
    for i in range(1, len(nodes)):
        # Find the last node on the rightmost path
        last = None
        current = root
        
        # Traverse to find the insertion point
        while current and current.value < nodes[i].value:
            last = current
            current = current.right
        
        # Insert the new node
        if not last:
            # New root
            nodes[i].left = root
            root = nodes[i]
        else:
            # Insert between last and current
            nodes[i].left = last.right
            last.right = nodes[i]
    
    return root

def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Args:
        arr (list): Input list of comparable elements
    
    Returns:
        list: Sorted list in ascending order
    """
    # Handle edge cases
    if not arr:
        return []
    
    if len(arr) == 1:
        return arr.copy()
    
    # Build Cartesian tree
    root = build_cartesian_tree(arr)
    
    # In-order traversal to get sorted elements
    def in_order_traversal(node, result):
        if not node:
            return
        
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)
    
    sorted_arr = []
    in_order_traversal(root, sorted_arr)
    
    return sorted_arr