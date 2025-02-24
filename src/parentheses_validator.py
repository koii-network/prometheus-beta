def is_balanced_parentheses(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.

    A string of parentheses is considered balanced if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    - The string may contain only parentheses

    Args:
        s (str): A string containing parentheses to validate

    Returns:
        bool: True if parentheses are balanced, False otherwise

    Examples:
        >>> is_balanced_parentheses("()")  # True
        >>> is_balanced_parentheses("((()))")  # True
        >>> is_balanced_parentheses("(())")  # True
        >>> is_balanced_parentheses(")(")  # False
        >>> is_balanced_parentheses("(()")  # False
        >>> is_balanced_parentheses("")  # True (empty string is considered balanced)
    """
    # Edge case: empty string is considered balanced
    if not s:
        return True
    
    # Only allow parentheses in the input
    if any(char not in '()' for char in s):
        return False
    
    # Track opening parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push opening parenthesis onto stack
            stack.append(char)
        else:  # char == ')'
            # If closing parenthesis with no matching opening, return False
            if not stack:
                return False
            
            # Remove last opening parenthesis
            stack.pop()
    
    # Balanced if stack is empty (all parentheses matched)
    return len(stack) == 0