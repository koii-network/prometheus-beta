def to_alternating_case(input_string):
    """
    Convert a string to alternating uppercase.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with alternating uppercase characters.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_case("hello")
        'HeLlO'
        >>> to_alternating_case("")
        ''
        >>> to_alternating_case("a")
        'A'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to alternating case
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(input_string)
    )