class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self._items) == 0

def reverse_list_with_stack(input_list):
    """
    Reverse a list of integers using a Stack data structure.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        input_list (list): List of integers to be reversed
    
    Returns:
        list: Reversed list
    """
    # Handle empty or None input
    if not input_list:
        return []
    
    # Create a stack
    stack = Stack()
    
    # Push all elements onto the stack
    for item in input_list:
        stack.push(item)
    
    # Create a new list by popping from the stack
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list