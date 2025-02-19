def alternating_camel_case(text: str) -> str:
    """
    Convert a given string to alternating camel case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating camel case.
    
    Examples:
        >>> alternating_camel_case("hello world")
        'hElLoWoRlD'
        >>> alternating_camel_case("python programming")
        'pYtHoNpRoGrAmMiNg'
        >>> alternating_camel_case("")
        ''
    """
    if not text:
        return ""
    
    result = []
    for i, char in enumerate(text.replace(" ", "")):
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    
    return ''.join(result)