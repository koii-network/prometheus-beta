def is_nested_parentheses(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string to check for nested parentheses
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        >>> is_nested_parentheses("()")  # Simple nested
        True
        >>> is_nested_parentheses("(())")  # Nested inside nested
        True
        >>> is_nested_parentheses(")(")  # Incorrect order
        False
        >>> is_nested_parentheses("(()")  # Unbalanced
        False
    """
    # Stack to track open parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push open parenthesis onto stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis and no open parentheses, it's invalid
            if not stack:
                return False
            
            # Pop the last open parenthesis
            stack.pop()
    
    # Stack should be empty for perfect nesting
    return len(stack) == 0