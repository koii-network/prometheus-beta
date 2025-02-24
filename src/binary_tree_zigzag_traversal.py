from typing import Optional, List, Any

class TreeNode:
    """
    Binary tree node class to represent the structure of the tree.
    
    Attributes:
        val: Value of the node
        left: Left child node
        right: Right child node
    """
    def __init__(self, val: Any = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order_traversal(root: Optional[TreeNode]) -> List[List[Any]]:
    """
    Perform a zigzag (spiral) level order traversal of a binary tree.
    
    In a zigzag traversal, nodes are traversed level by level, 
    alternating between left-to-right and right-to-left order.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree
    
    Returns:
        List[List[Any]]: A list of levels, where each level is a list of node values
        
    Time complexity: O(n), where n is the number of nodes in the tree
    Space complexity: O(n) to store the result and use the queue
    
    Examples:
        >>> root = TreeNode(3)
        >>> root.left = TreeNode(9)
        >>> root.right = TreeNode(20)
        >>> root.right.left = TreeNode(15)
        >>> root.right.right = TreeNode(7)
        >>> zigzag_level_order_traversal(root)
        [[3], [20, 9], [15, 7]]
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Initialize result list and queue
    result = []
    queue = [root]
    
    # Track the direction of traversal
    left_to_right = True
    
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            # Remove the first node from the queue
            node = queue.pop(0)
            
            # Add node to current level
            current_level.append(node.val)
            
            # Add child nodes to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level if traversing right to left
        if not left_to_right:
            current_level.reverse()
        
        # Add current level to result
        result.append(current_level)
        
        # Flip the traversal direction
        left_to_right = not left_to_right
    
    return result