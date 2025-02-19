def is_valid_parentheses(s: str) -> bool:
    """
    Determines if a string of parentheses is valid.
    
    A set of parentheses is valid if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses '(' and ')'
    
    Returns:
        bool: True if the parentheses are valid, False otherwise
    
    Examples:
        is_valid_parentheses("()") -> True
        is_valid_parentheses("()()") -> True
        is_valid_parentheses("(())") -> True
        is_valid_parentheses("(()") -> False
        is_valid_parentheses(")(") -> False
    """
    # Use a stack to track opening parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push opening parenthesis onto the stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis and no matching opening parenthesis, return False
            if not stack:
                return False
            
            # Remove the most recent opening parenthesis
            stack.pop()
    
    # Valid if all parentheses are matched (stack is empty)
    return len(stack) == 0