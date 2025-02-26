from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform a zigzag (spiral) level order traversal of a binary tree.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree.
    
    Returns:
        List[List[int]]: A list of levels, where each level is traversed 
        in alternating left-to-right and right-to-left directions.
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(n) to store the result and use the queue
    
    Examples:
        1. For a tree:    3
                        /   \
                       9    20
                           /  \
                          15   7
        Returns: [[3], [20,9], [15,7]]
        
        2. For an empty tree:
        Returns: []
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Initialize result list and queue
    result = []
    queue = [root]
    left_to_right = True
    
    # Traverse the tree level by level
    while queue:
        # Get the number of nodes at current level
        level_size = len(queue)
        current_level = [0] * level_size
        
        # Process all nodes at current level
        for i in range(level_size):
            # Remove the first node from the queue
            node = queue.pop(0)
            
            # Determine index based on traversal direction
            index = i if left_to_right else level_size - 1 - i
            current_level[index] = node.val
            
            # Add child nodes to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Add current level to result
        result.append(current_level)
        
        # Alternate traversal direction
        left_to_right = not left_to_right
    
    return result