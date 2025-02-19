def convert_to_alternating_caps(text: str) -> str:
    """
    Convert a string to alternating case (first char uppercase, next lowercase, and so on).
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The input string converted to alternating case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)