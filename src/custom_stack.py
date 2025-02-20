class CustomStack:
    def __init__(self, capacity=10):
        """
        Initialize a custom stack with a given capacity (default 10).
        
        Args:
            capacity (int, optional): Maximum number of elements the stack can hold. Defaults to 10.
        """
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        
        self._capacity = capacity
        self._items = []
    
    def push(self, item):
        """
        Push an item onto the stack.
        
        Args:
            item: Any data type to be added to the stack.
        
        Raises:
            OverflowError: If the stack is already at full capacity.
        """
        if len(self._items) >= self._capacity:
            raise OverflowError("Stack is full. Cannot push more items.")
        
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        
        return self._items.pop()
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        Returns:
            The top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def size(self):
        """
        Get the current number of items in the stack.
        
        Returns:
            int: Number of items in the stack.
        """
        return len(self._items)
    
    def capacity(self):
        """
        Get the maximum capacity of the stack.
        
        Returns:
            int: Maximum capacity of the stack.
        """
        return self._capacity