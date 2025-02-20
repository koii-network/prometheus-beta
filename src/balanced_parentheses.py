def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the input string are balanced.
    
    Args:
        s (str): Input string to check for balanced parentheses
    
    Returns:
        bool: True if all parentheses are balanced, False otherwise
    """
    # Stack to keep track of opening parentheses
    stack = []
    
    # Dictionary to map closing to opening parentheses
    parentheses_map = {')': '(', ']': '[', '}': '{'}
    
    # Set of opening parentheses
    opening_parentheses = set(parentheses_map.values())
    
    for char in s:
        # If it's an opening parenthesis, push to stack
        if char in opening_parentheses:
            stack.append(char)
        
        # If it's a closing parenthesis
        elif char in parentheses_map:
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            
            # Remove the matching opening parenthesis
            stack.pop()
    
    # Stack should be empty for all parentheses to be balanced
    return len(stack) == 0