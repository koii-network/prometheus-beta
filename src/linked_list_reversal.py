class Node:
    def __init__(self, value=0, next=None):
        """
        Initialize a node in the linked list.
        
        :param value: Value of the node (default 0)
        :param next: Reference to the next node (default None)
        """
        self.value = value
        self.next = next

def create_linked_list(n):
    """
    Create a linked list with n nodes.
    
    :param n: Number of nodes to create
    :return: Head of the created linked list
    """
    if n <= 0:
        return None
    
    # Create the head node
    head = Node(1)
    current = head
    
    # Create subsequent nodes
    for i in range(2, n + 1):
        current.next = Node(i)
        current = current.next
    
    return head

def append_node(head, value):
    """
    Append a new node to the end of the linked list.
    
    :param head: Head of the linked list
    :param value: Value of the new node to append
    :return: Head of the modified linked list
    """
    if not head:
        return Node(value)
    
    current = head
    while current.next:
        current = current.next
    
    current.next = Node(value)
    return head

def reverse_linked_list(head, n):
    """
    Reverse the first n nodes of the linked list.
    
    :param head: Head of the linked list
    :param n: Number of nodes to reverse
    :return: New head of the modified linked list
    """
    # Handle edge cases
    if not head or n <= 1:
        return head
    
    # Track the previous, current, and next nodes
    prev = None
    current = head
    count = 0
    
    # Reverse first n nodes
    while current and count < n:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
        count += 1
    
    # Connect the reversed part with the rest of the list
    if head:
        head.next = current
    
    return prev

def linked_list_to_list(head):
    """
    Convert linked list to a regular list for easy comparison.
    
    :param head: Head of the linked list
    :return: List representation of the linked list
    """
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result