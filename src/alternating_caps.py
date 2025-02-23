def to_alternating_caps(input_string):
    """
    Convert a string to alternating capitalization case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_caps("hello")
        'HeLlO'
        >>> to_alternating_caps("python")
        'PyThOn'
        >>> to_alternating_caps("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating caps, but only for alphabetic characters
    result = []
    is_upper = True
    for char in input_string:
        if char.isalpha():
            # Toggle case for alphabetic characters
            if is_upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            is_upper = not is_upper
        else:
            # Non-alphabetic characters stay the same
            result.append(char)
    
    return ''.join(result)