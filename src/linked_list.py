class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a linked list in-place.
    
    Args:
        head (ListNode): The head of the linked list.
    
    Returns:
        ListNode: The new head of the reversed linked list.
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize pointers for in-place reversal
    prev = None
    current = head
    
    while current:
        # Store the next node before changing links
        next_node = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers one step forward
        prev = current
        current = next_node
    
    # Return the new head (last node of original list)
    return prev