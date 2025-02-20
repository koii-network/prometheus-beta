class CustomStack:
    def __init__(self, capacity=10):
        """
        Initialize a custom stack with a given capacity.
        
        :param capacity: Maximum number of elements the stack can hold (default 10)
        """
        self._capacity = capacity
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        :param item: Any data type to be added to the stack
        :raises ValueError: If the stack is already at full capacity
        """
        if len(self._items) >= self._capacity:
            raise ValueError("Stack is full. Cannot push more items.")
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        :return: The top item from the stack
        :raises IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()
    
    def peek(self):
        """
        Return the top item from the stack without removing it.
        
        :return: The top item from the stack
        :raises IndexError: If the stack is empty
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