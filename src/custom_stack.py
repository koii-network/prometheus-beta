class CustomStack:
    def __init__(self, capacity=10):
        """
        Initialize a custom stack with a fixed capacity.
        
        :param capacity: Maximum number of elements the stack can hold (default 10)
        """
        if capacity <= 0:
            raise ValueError("Stack capacity must be a positive integer")
        
        self._capacity = capacity
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        :param item: Any data type to be added to the stack
        :raises OverflowError: If the stack is already at maximum capacity
        """
        if len(self._items) >= self._capacity:
            raise OverflowError("Stack is full. Cannot push more items.")
        
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        :raises IndexError: If the stack is empty
        :return: The top item from the stack
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        
        return self._items.pop()
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        :raises IndexError: If the stack is empty
        :return: The top item from the stack
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty stack")
        
        return self._items[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        :return: True if the stack is empty, False otherwise
        """
        return len(self._items) == 0
    
    def __len__(self):
        """
        Return the current number of items in the stack.
        
        :return: Number of items in the stack
        """
        return len(self._items)
    
    def capacity(self):
        """
        Return the maximum capacity of the stack.
        
        :return: Maximum number of items the stack can hold
        """
        return self._capacity