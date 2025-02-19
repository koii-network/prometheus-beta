def validate_parentheses(s: str) -> bool:
    """
    Check if the parentheses in the given string are balanced.
    
    Args:
        s (str): A string containing parentheses
    
    Returns:
        bool: True if parentheses are balanced, False otherwise
    """
    # Use a stack to track opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If it's an opening parenthesis, push to stack
        if char == '(':
            stack.append(char)
        # If it's a closing parenthesis
        elif char == ')':
            # If stack is empty, no matching opening parenthesis
            if not stack:
                return False
            # Pop the last opening parenthesis
            stack.pop()
    
    # Stack should be empty for perfectly balanced parentheses
    return len(stack) == 0