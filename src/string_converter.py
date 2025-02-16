def convert_to_alternating_lower(input_string):
    """
    Convert a string to specific alternating lower case pattern.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with specific alternating case pattern.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(input_string):
        # Even-indexed characters are lowercased, 
        # odd-indexed characters remain unchanged
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char)
    
    return ''.join(result)