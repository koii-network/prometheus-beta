def convert_to_header_case(input_string: str) -> str:
    """
    Convert a given string to header case.
    
    Header case is a title-like formatting where:
    - First letter of each word is capitalized
    - Words are separated by spaces
    - Handles various input formats like snake_case, kebab-case, camelCase, etc.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to header case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
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
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Replace separators and split
    # Replace underscores, hyphens, and handle camelCase
    normalized = input_string.replace('_', ' ').replace('-', ' ')
    
    # Handle camelCase by inserting spaces before capital letters
    chars = []
    for i, char in enumerate(normalized):
        if i > 0 and char.isupper() and normalized[i-1].islower():
            chars.append(' ')
        chars.append(char)
    
    # Join and convert to header case (capitalize each word)
    return ' '.join(word.capitalize() for word in ''.join(chars).split())