def is_parentheses_nested(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string to check for correct parentheses nesting
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        >>> is_parentheses_nested("()")  # Simple matching
        True
        >>> is_parentheses_nested("(())")  # Nested parentheses
        True
        >>> is_parentheses_nested("(()())")  # Multiple nested
        True
        >>> is_parentheses_nested("(()")  # Unbalanced
        False
        >>> is_parentheses_nested(")("  # Incorrect order
        False
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push opening parentheses onto stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis when stack is empty, it's unbalanced
            if not stack:
                return False
            
            # Remove last opening parenthesis
            stack.pop()
    
    # Stack should be empty for perfectly nested parentheses
    return len(stack) == 0