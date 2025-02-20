def is_balanced_parentheses(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string to check for balanced parentheses
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        >>> is_balanced_parentheses("()")
        True
        >>> is_balanced_parentheses("(())")
        True
        >>> is_balanced_parentheses("()()")
        True
        >>> is_balanced_parentheses("(()())")
        True
        >>> is_balanced_parentheses("(()")
        False
        >>> is_balanced_parentheses("())")
        False
        >>> is_balanced_parentheses(")(")
        False
    """
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0