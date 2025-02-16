def to_alternating_constant_case(input_string):
    """
    Convert a string to alternating constant case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating constant case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)