def to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_dot_case("hello world")
        'hElLo.wOrLd'
        >>> to_alternating_dot_case("PYTHON")
        'pYtHoN'
        >>> to_alternating_dot_case("")
        ''
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to alternating dot case
    result = []
    for i, char in enumerate(input_string):
        # Alternate case based on index
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    
    return ''.join(result)