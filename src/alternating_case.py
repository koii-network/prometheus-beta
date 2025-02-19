def to_alternating_case(input_string):
    """
    Convert a string to alternating case (first character uppercase, 
    subsequent characters lowercase, alternating).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)