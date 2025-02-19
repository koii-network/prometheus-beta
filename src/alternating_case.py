def to_alternating_lower_case(input_string):
    """
    Convert a string to alternating lower case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with alternating lower case letters.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return ''.join(char.lower() if idx % 2 == 0 else char.upper() 
                   for idx, char in enumerate(input_string.lower()))