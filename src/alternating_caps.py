def to_alternating_caps(text):
    """
    Convert a string to alternating caps case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        # Even indices (0, 2, 4...) will be uppercase
        # Odd indices (1, 3, 5...) will be lowercase
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)