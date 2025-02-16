def to_alternating_case(text):
    """
    Convert a string to alternating case (uppercase and lowercase).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating case characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return empty string
    if not text:
        return ""
    
    # Convert to alternating case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )