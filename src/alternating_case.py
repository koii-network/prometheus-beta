def convert_to_alternating_case(input_string):
    """
    Convert a string to alternating uppercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if index % 2 == 0 else char.lower() 
        for index, char in enumerate(input_string)
    )