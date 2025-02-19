def convert_to_alternating_case(text):
    """
    Convert a string to alternating case (upper and lower).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )