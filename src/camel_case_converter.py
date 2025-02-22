def to_camel_case(string: str) -> str:
    """
    Convert a string to camel case.
    
    Args:
        string (str): Input string to convert. 
                      Supports inputs with spaces, hyphens, or underscores.
    
    Returns:
        str: Camel case version of the input string.
    
    Examples:
        >>> to_camel_case("hello world")
        'helloWorld'
        >>> to_camel_case("hello-world")
        'helloWorld'
        >>> to_camel_case("hello_world")
        'helloWorld'
    """
    # Handle empty or None input
    if not string:
        return ""
    
    # Replace hyphens and underscores with spaces
    string = string.replace('-', ' ').replace('_', ' ')
    
    # Split the string into words
    words = string.split()
    
    # Capitalize all words except the first
    result = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    return result