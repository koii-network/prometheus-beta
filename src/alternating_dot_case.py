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
        'hElLo.WoRlD'
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
    should_be_lower = True
    for char in input_string:
        if char.isalpha():
            # Apply alternating case to alphabetic characters
            result.append(char.lower() if should_be_lower else char.upper())
            should_be_lower = not should_be_lower
        elif char.isdigit():
            # Treat each digit as an alternating uppercase letter
            result.append('NeXtC')
        else:
            # Non-alphabetic characters get a dot
            result.append('.')
    
    return ''.join(result)