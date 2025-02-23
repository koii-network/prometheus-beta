class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a linked list by changing the direction of node pointers.
    
    Args:
        head (ListNode): The head of the original linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None
    current = head
    
    # Traverse the list and reverse pointers
    while current:
        # Store the next node before changing pointers
        next_node = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers one step forward
        prev = current
        current = next_node
    
    # Return the new head (previously the last node)
    return prev