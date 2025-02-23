def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the input string are balanced.
    
    Args:
        s (str): Input string to check for balanced parentheses
    
    Returns:
        bool: True if all parentheses are balanced, False otherwise
    """
    # Define mapping of closing to opening parentheses
    parentheses_map = {')': '(', ']': '[', '}': '{'}
    
    # Stack to track opening parentheses
    stack = []
    
    for char in s:
        # If it's a closing parenthesis
        if char in parentheses_map:
            # If stack is empty or top doesn't match corresponding opening parenthesis
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            # Remove the matching opening parenthesis
            stack.pop()
        
        # If it's an opening parenthesis, push to stack
        elif char in '([{':
            stack.append(char)
    
    # If stack is empty, all parentheses are balanced
    return len(stack) == 0