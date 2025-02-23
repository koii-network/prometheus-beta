def is_valid_parentheses(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string to validate parentheses nesting
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        >>> is_valid_parentheses("()")
        True
        >>> is_valid_parentheses("(())")
        True
        >>> is_valid_parentheses("(()())")
        True
        >>> is_valid_parentheses("(()")
        False
        >>> is_valid_parentheses(")(")
        False
        >>> is_valid_parentheses("")
        True
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        if char == '(':
            # Push opening parenthesis onto the stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis and no matching opening parenthesis, return False
            if not stack:
                return False
            
            # Remove the last opening parenthesis from the stack
            stack.pop()
    
    # Return True if stack is empty (all parentheses matched), False otherwise
    return len(stack) == 0