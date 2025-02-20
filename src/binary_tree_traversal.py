from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform a zigzag level order traversal of a binary tree.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree.
    
    Returns:
        List[List[int]]: A list of lists, where each inner list represents 
                         a level of the tree, with alternating left-to-right 
                         and right-to-left order.
    """
    # If the tree is empty, return an empty list
    if not root:
        return []
    
    # Use a queue to perform level-order traversal
    queue = [root]
    result = []
    left_to_right = True
    
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            # Remove the first node from the queue
            node = queue.pop(0)
            
            # Add the node's value to the current level
            current_level.append(node.val)
            
            # Add child nodes to the queue for next iteration
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level if we're in a right-to-left traversal
        if not left_to_right:
            current_level.reverse()
        
        # Add the current level to the result
        result.append(current_level)
        
        # Alternate traversal direction
        left_to_right = not left_to_right
    
    return result