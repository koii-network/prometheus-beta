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
    Reverses the order of elements in a list using a Stack data structure.
    
    Args:
        input_list (list): The list of integers to be reversed.
    
    Returns:
        list: A new list with elements in reverse order.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Handle empty or None input
    if not input_list:
        return []
    
    # Create a stack
    stack = Stack()
    
    # Push all elements to the stack
    for item in input_list:
        stack.push(item)
    
    # Create a new list by popping from stack
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list