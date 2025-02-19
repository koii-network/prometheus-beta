def is_balanced_parentheses(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.
    
    Args:
        s (str): A string containing parentheses
    
    Returns:
        bool: True if parentheses are balanced, False otherwise
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