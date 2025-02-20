def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the given string are balanced.
    
    Args:
        s (str): Input string to check for balanced parentheses
    
    Returns:
        bool: True if all parentheses are balanced, False otherwise
    """
    # Dictionary to map closing to opening parentheses
    parentheses_map = {')': '(', ']': '[', '}': '{'}
    
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If character is a closing parenthesis
        if char in parentheses_map:
            # If stack is empty or top of stack doesn't match corresponding opening parenthesis
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            # Remove the matching opening parenthesis from stack
            stack.pop()
        
        # If character is an opening parenthesis, push to stack
        elif char in ['(', '[', '{']:
            stack.append(char)
    
    # Stack should be empty if all parentheses are balanced
    return len(stack) == 0