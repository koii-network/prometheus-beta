def alternating_header_case(text: str) -> str:
    """
    Convert a string to alternating header case.
    
    In alternating header case, each character alternates between 
    uppercase and lowercase, starting with uppercase.
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The string converted to alternating header case
    
    Examples:
        >>> alternating_header_case("hello world")
        'HeLlO WoRlD'
        >>> alternating_header_case("")
        ''
        >>> alternating_header_case("a")
        'A'
    """
    if not text:
        return text
    
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(text)
    )