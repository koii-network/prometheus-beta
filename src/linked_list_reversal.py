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
    Reverse a singly linked list by changing the direction of node pointers.
    
    Args:
        head (ListNode): The head of the original linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as reversal is done in-place
    
    Edge Cases:
    - If the list is empty (head is None), return None
    - If the list has only one node, return that node
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None  # Previous node, initially None
    current = head  # Current node being processed
    
    # Traverse the list and reverse pointers
    while current:
        # Store the next node before changing pointers
        next_node = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers one step forward
        prev = current
        current = next_node
    
    # Return the new head (last node of original list)
    return prev