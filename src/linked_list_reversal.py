class ListNode:
    """
    Represents a node in a singly linked list.
    
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
        head (ListNode): The head of the linked list to be reversed.
    
    Returns:
        ListNode: The new head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as the reversal is done in-place
    
    Examples:
        # Empty list
        >>> reverse_linked_list(None) is None
        True
        
        # Single node list
        >>> single_node = ListNode(1)
        >>> result = reverse_linked_list(single_node)
        >>> result.val
        1
        >>> result.next is None
        True
        
        # Multiple node list
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> result = reverse_linked_list(head)
        >>> result.val
        3
        >>> result.next.val
        2
        >>> result.next.next.val
        1
        >>> result.next.next.next is None
        True
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize pointers for in-place reversal
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
    
    # Return the new head (previously the last node)
    return prev