class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list and returns the new head.
    
    Args:
        head (ListNode): The head of the input linked list
    
    Returns:
        ListNode: The head of the reversed linked list
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    prev = None
    current = head
    
    while current:
        # Store the next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move prev and current one step forward
        prev = current
        current = next_node
    
    # prev is now the new head
    return prev