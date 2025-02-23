def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to constant case (UPPERCASE_WITH_UNDERSCORES).
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to constant case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("camelCaseString")
        'CAMEL_CASE_STRING'
        >>> to_constant_case("snake_case_string")
        'SNAKE_CASE_STRING'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert string to constant case
    converted_chars = []
    for i, char in enumerate(input_string):
        # Add underscore before capital letters (except the first character)
        if i > 0 and char.isupper():
            converted_chars.append('_')
        
        # Replace non-alphanumeric characters with underscores
        if not char.isalnum():
            converted_chars.append('_')
        else:
            converted_chars.append(char.upper())
    
    # Remove consecutive underscores and strip leading/trailing underscores
    return '_'.join(filter(bool, ''.join(converted_chars).split('_')))