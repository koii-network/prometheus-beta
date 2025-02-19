def to_header_case(text: str) -> str:
    """
    Convert a string to header case (title case with special handling for certain separators).
    
    Args:
        text (str): The input string to convert to header case.
    
    Returns:
        str: The input string converted to header case.
    
    Examples:
        >>> to_header_case("hello world")
        'Hello World'
        >>> to_header_case("hello-world")
        'Hello World'
        >>> to_header_case("hello_world")
        'Hello World'
        >>> to_header_case("hello.world")
        'Hello World'
    """
    # Replace common separators with spaces
    normalized = text.replace('-', ' ').replace('_', ' ').replace('.', ' ')
    
    # Split the string, capitalize each word, and join
    return ' '.join(word.capitalize() for word in normalized.split())