def is_valid_parentheses(s: str) -> bool:
    """
    Determine if a string of parentheses is valid.
    
    A string is considered valid if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses characters '(' and ')'
    
    Returns:
        bool: True if the parentheses are valid, False otherwise
    """
    # Track the number of open parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push opening parenthesis onto the stack
            stack.append(char)
        elif char == ')':
            # If trying to close when no open parentheses exist, it's invalid
            if not stack:
                return False
            
            # Remove the most recent open parenthesis
            stack.pop()
    
    # Valid if all parentheses have been matched (stack is empty)
    return len(stack) == 0