class CustomStack:
    """
    A custom stack data structure with a fixed capacity of 10 elements.
    Supports any data type and provides standard stack operations.
    """
    def __init__(self, capacity=10):
        """
        Initialize the stack with a given capacity (default 10).
        
        :param capacity: Maximum number of elements the stack can hold
        """
        self.capacity = capacity
        self.items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        :param item: Any data type to be added to the stack
        :raises ValueError: If the stack is already at full capacity
        """
        if len(self.items) >= self.capacity:
            raise ValueError("Stack is full. Cannot push more items.")
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        :return: The top item of the stack
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item of the stack without removing it.
        
        :return: The top item of the stack
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack.")
        return self.items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        :return: True if the stack is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Return the current number of items in the stack.
        
        :return: Number of items in the stack
        """
        return len(self.items)