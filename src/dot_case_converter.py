def convert_to_dot_case(input_string):
    """
    Convert a given string to dot case.
    
    Dot case is a string formatting where words are separated by dots,
    and all characters are lowercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to dot case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_dot_case("HelloWorld")
        'hello.world'
        >>> convert_to_dot_case("snake_case_string")
        'snake.case.string'
        >>> convert_to_dot_case("CamelCaseString")
        'camel.case.string'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert string to lowercase
    lowercase_str = input_string.lower()
    
    # Replace common separators with dots
    replacements = [
        ('_', '.'),   # snake_case
        ('-', '.'),   # kebab-case
        (' ', '.'),   # space-separated
    ]
    
    # Apply replacements
    for old, new in replacements:
        lowercase_str = lowercase_str.replace(old, '.')
    
    # Handle camelCase and PascalCase
    result = []
    for i, char in enumerate(lowercase_str):
        # Add dot before uppercase letters (in original input)
        if (i > 0 and 
            input_string[i].isupper() and 
            input_string[i-1].islower()):
            result.append('.')
        result.append(char)
    
    # Convert to string and remove consecutive dots
    final_str = ''.join(result)
    while '..' in final_str:
        final_str = final_str.replace('..', '.')
    
    # Remove leading or trailing dots
    return final_str.strip('.')