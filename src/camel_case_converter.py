def to_camel_case(text: str) -> str:
    """
    Convert a string to camel case.
    
    Args:
        text (str): Input string to convert. Can be space, hyphen, or underscore separated.
    
    Returns:
        str: Camel case version of the input string.
    
    Examples:
        >>> to_camel_case('hello world')
        'helloWorld'
        >>> to_camel_case('hello-world')
        'helloWorld'
        >>> to_camel_case('hello_world')
        'helloWorld'
    """
    # Handle empty string case
    if not text:
        return ''
    
    # Replace hyphens and underscores with spaces
    words = text.replace('-', ' ').replace('_', ' ').split()
    
    # Capitalize all words except the first
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])