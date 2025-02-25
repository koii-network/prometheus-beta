class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (Any): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a new ListNode.
        
        Args:
            val (Any, optional): Value to be stored in the node. Defaults to 0.
            next (ListNode, optional): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next


def reverse_linked_list(head):
    """
    Reverse a singly linked list by changing the direction of node pointers.
    
    This function reverses the linked list in-place with O(n) time complexity 
    and O(1) space complexity.
    
    Args:
        head (ListNode): The head of the input linked list.
    
    Returns:
        ListNode: The new head of the reversed linked list.
    
    Examples:
        >>> original = ListNode(1, ListNode(2, ListNode(3)))
        >>> reversed_list = reverse_linked_list(original)
        >>> # reversed_list now points to 3 -> 2 -> 1 -> None
    """
    # Handle empty list or single node cases
    if not head or not head.next:
        return head
    
    # Initialize pointers
    prev = None
    current = head
    
    # Iterate through the list and reverse pointers
    while current:
        # Store the next node before changing pointers
        next_node = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (previously the last node)
    return prev