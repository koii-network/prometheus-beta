class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome_linked_list(head):
    """
    Determine whether a given linked list is palindromic.
    
    Args:
        head (ListNode): The head of the linked list
    
    Returns:
        bool: True if the linked list is palindromic, False otherwise
    """
    # If the list is empty or has only one node, it's a palindrome
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
        temp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = temp
    
    # Step 3: Compare the first half with the reversed second half
    first_half = head
    second_half = prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True