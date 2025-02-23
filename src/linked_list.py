class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a singly linked list in-place.
    
    Args:
        head (ListNode): The head of the linked list.
    
    Returns:
        ListNode: The new head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes
    Space Complexity: O(1), as reversal is done in-place
    
    Handles cases:
    - Empty list (head is None)
    - Single node list
    - Multiple node list
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize pointers
    prev = None
    current = head
    
    # Traverse and reverse links
    while current:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # prev is now the new head
    return prev