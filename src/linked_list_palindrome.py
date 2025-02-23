class ListNode:
    """
    A class representing a node in a linked list.
    
    Attributes:
        val (any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome_linked_list(head):
    """
    Determines whether a given linked list is palindromic.
    
    Args:
        head (ListNode): The head of the linked list.
    
    Returns:
        bool: True if the linked list is palindromic, False otherwise.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Raises:
        TypeError: If the input is not a valid linked list.
    """
    # Handle edge cases
    if head is None or head.next is None:
        return True
    
    # Find the middle of the linked list
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the list
    second_half = reverse_list(slow.next)
    
    # Compare first half with reversed second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

def reverse_list(head):
    """
    Reverses a linked list in-place.
    
    Args:
        head (ListNode): The head of the linked list to reverse.
    
    Returns:
        ListNode: The new head of the reversed list.
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev