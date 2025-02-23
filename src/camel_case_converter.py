def to_camel_case(input_string: str) -> str:
    """
    Convert a string to camel case.
    
    Args:
        input_string (str): The input string to convert to camel case.
    
    Returns:
        str: The camel case version of the input string.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_camel_case("hello world")
        'helloWorld'
        >>> to_camel_case("hello-world")
        'helloWorld'
        >>> to_camel_case("hello_world")
        'helloWorld'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return empty string
    if not input_string:
        return ""
    
    # Replace underscores and hyphens with spaces
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string into words
    words = normalized.split()
    
    # Capitalize all words except the first
    camel_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    # Join the words together
    return ''.join(camel_words)