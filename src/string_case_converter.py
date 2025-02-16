def alternating_constant_case(text):
    """
    Convert a string to alternating constant case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating constant case.
    
    Examples:
        >>> alternating_constant_case("hello world")
        'HELLO world'
        >>> alternating_constant_case("python is awesome")
        'PYTHON is AWESOME'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    words = text.split()
    return ' '.join(word.upper() if i % 2 == 0 else word.lower() 
                    for i, word in enumerate(words))