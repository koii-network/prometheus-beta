def convert_to_header_case(input_string):
    """
    Convert a given string to header case.
    
    Header case capitalizes the first letter of each word, 
    removing any existing capitalization and handling various 
    input formats like snake_case, kebab-case, or camelCase.
    
    Args:
        input_string (str): The input string to convert to header case.
    
    Returns:
        str: The input string converted to header case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    
    Examples:
        >>> convert_to_header_case("hello world")
        'Hello World'
        >>> convert_to_header_case("hello_world")
        'Hello World'
        >>> convert_to_header_case("hello-world")
        'Hello World'
        >>> convert_to_header_case("helloWorld")
        'Hello World'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Replace non-word characters with spaces
    import re
    
    # Convert camelCase and PascalCase to space-separated
    # Use regex to insert space before capital letters, except at the start
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
    
    # Replace underscores, hyphens, and multiple spaces with single space
    normalized = re.sub(r'[_\-]+', ' ', s2)
    normalized = re.sub(r'\s+', ' ', normalized)
    
    # Split, capitalize each word, and join
    return ' '.join(word.capitalize() for word in normalized.split())