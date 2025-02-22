class Node:
    """
    Represents a node in a linked list.
    
    Attributes:
        value (int): The value stored in the node.
        next (Node): Reference to the next node in the list.
    """
    def __init__(self, value):
        """
        Initialize a new Node.
        
        Args:
            value (int): The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a linked list with methods to create, append, and reverse.
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
            value (int): The value to be added to the list.
        """
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def create_list(self, n):
        """
        Create a linked list with n nodes, where each node's value is its index.
        
        Args:
            n (int): Number of nodes to create in the list.
        """
        for i in range(n):
            self.append(i)
    
    def reverse(self):
        """
        Reverse the order of nodes in the linked list.
        """
        prev = None
        current = self.head
        
        while current:
            # Store the next node
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers one step forward
            prev = current
            current = next_node
        
        # Update head to the new first node
        self.head = prev
    
    def to_list(self):
        """
        Convert the linked list to a Python list for easy verification.
        
        Returns:
            list: A list of node values in order.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result