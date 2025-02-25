class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (any): The value stored in the node.
        next (ListNode): Reference to the next node in the list.
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.
        
        Args:
            val (any, optional): Value to be stored in the node. Defaults to 0.
            next (ListNode, optional): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list by changing the direction of node pointers.
    
    Args:
        head (ListNode): The head of the original linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None  # Previous node (will become new tail)
    current = head  # Current node being processed
    
    # Traverse and reverse links
    while current:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (which was previously the last node)
    return prev