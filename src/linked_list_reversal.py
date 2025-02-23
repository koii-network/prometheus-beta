class Node:
    """
    Represents a node in a singly linked list.
    
    Attributes:
        value: The value stored in the node
        next: Reference to the next node in the list (None if last node)
    """
    def __init__(self, value=None):
        """
        Initialize a new Node.
        
        Args:
            value: The value to be stored in the node (default: None)
        """
        self.value = value
        self.next = None


class LinkedList:
    """
    A singly linked list implementation with reversal functionality.
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
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def reverse(self, n=None):
        """
        Reverse the linked list, optionally limiting to first n nodes.
        
        Args:
            n (int, optional): Number of nodes to reverse. 
                               If None, reverse entire list.
        
        Raises:
            ValueError: If n is negative or exceeds list length
        """
        # Handle empty list
        if not self.head:
            return
        
        # Validate n if provided
        if n is not None:
            if n < 0:
                raise ValueError("Number of nodes to reverse cannot be negative")
            
            # Count total nodes
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            
            if n > count:
                raise ValueError(f"Cannot reverse {n} nodes in a list with {count} nodes")
        
        # Reverse logic
        prev = None
        current = self.head
        count = 0
        
        while current and (n is None or count < n):
            # Store next node before changing links
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
            count += 1
        
        # If reversing partial list, reconnect remaining part
        if n is not None and current:
            # Head's next should point to the remaining part
            self.head.next = current
        
        # Update head to new start
        self.head = prev
    
    def to_list(self):
        """
        Convert linked list to a Python list for easy comparison.
        
        Returns:
            list: Values of nodes in order
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result


def create_linked_list(n):
    """
    Create a linked list with n nodes containing values 1 to n.
    
    Args:
        n (int): Number of nodes to create
    
    Returns:
        LinkedList: A linked list with n nodes
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Number of nodes cannot be negative")
    
    ll = LinkedList()
    for i in range(1, n+1):
        ll.append(i)
    
    return ll