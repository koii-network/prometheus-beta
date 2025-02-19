def alternating_header_case(text):
    """
    Convert a string to alternating header case.
    
    Args:
        text (str): The input string to be converted.
    
    Returns:
        str: A string with alternating uppercase and lowercase letters.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> alternating_header_case("hello world")
        'HeLlO WoRlD'
        >>> alternating_header_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)