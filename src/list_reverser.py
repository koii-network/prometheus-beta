class Stack:
    """
    A simple Stack data structure implementation using a list.
    
    This implementation provides basic stack operations like push, pop, 
    and checking if the stack is empty.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
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
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0


def reverse_list_with_stack(input_list):
    """
    Reverse the order of elements in a list using a Stack.
    
    This function uses a stack to efficiently reverse the order of elements
    in the input list. It works with lists of any length, including 
    empty lists and lists with a single element.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        input_list (list): The list to be reversed.
    
    Returns:
        list: A new list with elements in reversed order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Validate input
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Create a new stack
    stack = Stack()
    
    # Push all elements to the stack
    for item in input_list:
        stack.push(item)
    
    # Create a new list to store reversed elements
    reversed_list = []
    
    # Pop elements from stack to create reversed list
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list