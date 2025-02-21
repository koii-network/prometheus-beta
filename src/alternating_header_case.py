def to_alternating_header_case(text):
    """
    Convert a string to alternating header case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating header case.
    
    Examples:
        >>> to_alternating_header_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_header_case("python is awesome")
        'PyThOn Is AwEsOmE'
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