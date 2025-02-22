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
    
    # prev is now the new head of the reversed list
    return prev

def list_to_array(head):
    """
    Convert a linked list to an array for easier testing and comparison.
    
    Args:
        head (ListNode): The head of the input linked list
    
    Returns:
        list: An array representation of the linked list
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def array_to_linked_list(arr):
    """
    Convert an array to a linked list.
    
    Args:
        arr (list): An input array
    
    Returns:
        ListNode: The head of the created linked list
    """
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head