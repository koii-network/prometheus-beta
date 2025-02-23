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
    
    # Convert to alternating caps
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(input_string)
    )