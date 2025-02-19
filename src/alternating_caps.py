def to_alternating_caps(text):
    """
    Convert a string to alternating caps case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string with alternating capitalization.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return an empty string
    if not text:
        return ""
    
    # Convert to alternating caps
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )