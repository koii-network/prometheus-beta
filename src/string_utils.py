def to_title_case(input_string: str) -> str:
    """
    Convert a string to title case.
    
    Args:
        input_string (str): The input string to convert to title case.
    
    Returns:
        str: The input string converted to title case.
    
    Examples:
        >>> to_title_case("hello world")
        'Hello World'
        >>> to_title_case("PYTHON PROGRAMMING")
        'Python Programming'
        >>> to_title_case("python-programming-language")
        'Python-Programming-Language'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the string by spaces and hyphens, then capitalize each word
    words = input_string.replace('-', ' ').split()
    return ' '.join(word.capitalize() for word in words).replace(' ', '-') if '-' in input_string else ' '.join(word.capitalize() for word in words)