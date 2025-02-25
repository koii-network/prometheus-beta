class Node:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        value: The value stored in the node
        next: Reference to the next node in the list (None if last node)
    """
    def __init__(self, value=None):
        """
        Initialize a node with an optional value.
        
        Args:
            value: The value to be stored in the node (default is None)
        """
        self.value = value
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list with basic operations.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
    
    def append(self, value):
        """
        Append a new node with the given value to the end of the list.
        
        Args:
            value: The value to be added to the list
        """
        new_node = Node(value)
        
        # If the list is empty, set the new node as head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Add the new node
        current.next = new_node
    
    def reverse_list(self):
        """
        Reverse the order of nodes in the linked list.
        
        Returns:
            None. The list is modified in-place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Handle empty list or single node list
        if not self.head or not self.head.next:
            return
        
        prev = None
        current = self.head
        
        while current:
            # Store the next node before changing links
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
        
        # Update head to the new start (previous last node)
        self.head = prev
    
    def to_list(self):
        """
        Convert the linked list to a Python list for easy comparison.
        
        Returns:
            A list containing the values of nodes in order
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def create_linked_list(n):
    """
    Create a linked list with n nodes, each node having a value from 1 to n.
    
    Args:
        n (int): Number of nodes to create in the list
    
    Returns:
        LinkedList: A linked list with n nodes
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number of nodes cannot be negative")
    
    linked_list = LinkedList()
    for i in range(1, n + 1):
        linked_list.append(i)
    
    return linked_list