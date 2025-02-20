def is_correctly_nested(s: str) -> bool:
    """
    Determine if parentheses in a string are correctly nested.
    
    Args:
        s (str): Input string to check for correct parentheses nesting
    
    Returns:
        bool: True if parentheses are correctly nested, False otherwise
    
    Examples:
        - '()' -> True
        - '((()))' -> True
        - '(()())' -> True
        - '(' -> False
        - ')' -> False
        - '())' -> False
        - '((()' -> False
    """
    # Stack to keep track of open parentheses
    stack = []
    
    for char in s:
        if char == '(':
            # Push open parenthesis to stack
            stack.append(char)
        elif char == ')':
            # If closing parenthesis and no open parentheses, return False
            if not stack:
                return False
            
            # Pop the last open parenthesis
            stack.pop()
    
    # Return True only if stack is empty (all parentheses matched)
    return len(stack) == 0