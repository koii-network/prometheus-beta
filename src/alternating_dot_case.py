def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_alternating_dot_case("hello world")
        'h.E.l.L.o. .W.o.R.l.D'
        >>> convert_to_alternating_dot_case("Python")
        'p.Y.t.H.o.N'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating dot case
    result = []
    current_case_index = 0  # Maintain global case across entire string

    for char in input_string:
        if char.isalnum() or char.isspace() or char in '-!':
            # Apply alternating case
            if current_case_index % 2 == 0:
                result.append(char.lower())
            else:
                result.append(char.upper())
            
            # Increment case index for alphanumeric characters
            if char.isalnum():
                current_case_index += 1
        
        # Always add a dot after each character except the last
        if len(result) < len(input_string) * 2 - 1:
            result.append('.')
    
    return ''.join(result)