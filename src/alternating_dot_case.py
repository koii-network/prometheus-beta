def to_alternating_dot_case(text):
    """
    Convert a string to alternating dot case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        # If character is a letter, convert to dot case
        if char.isalpha():
            if i % 2 == 0:
                result.append(char.lower())
            else:
                result.append('.' + char.upper())
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)