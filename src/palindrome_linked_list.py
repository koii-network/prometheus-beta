class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindromic_linked_list(head):
    """
    Determine if a linked list is palindromic.
    
    Args:
        head (ListNode): The head of the linked list
    
    Returns:
        bool: True if the linked list is palindromic, False otherwise
    """
    # Handle empty or single node list
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle of the linked list
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the list
    second_half = slow.next
    prev = None
    while second_half:
        next_node = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = next_node
    slow.next = prev
    
    # Step 3: Compare first and second half
    first_half = head
    second_half = slow.next
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True