def is_valid_parentheses(s: str) -> bool:
    """
    Determines if a string of parentheses is valid.
    
    A string is considered valid if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Closing parentheses occur in the correct order
    
    Args:
        s (str): A string containing only parentheses characters '(' and ')'
    
    Returns:
        bool: True if the parentheses are valid, False otherwise
    
    Examples:
        is_valid_parentheses("()") -> True
        is_valid_parentheses("(())") -> True
        is_valid_parentheses("(()())") -> True
        is_valid_parentheses("(()") -> False
        is_valid_parentheses(")(") -> False
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        if char == '(':
            # Push opening parenthesis onto the stack
            stack.append(char)
        elif char == ')':
            # If we see a closing parenthesis but no opening ones, it's invalid
            if not stack:
                return False
            
            # Pop the last opening parenthesis
            stack.pop()
    
    # The string is valid only if the stack is empty at the end
    return len(stack) == 0