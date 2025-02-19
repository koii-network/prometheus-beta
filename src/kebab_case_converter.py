def convert_to_kebab_case(input_string: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to kebab-case.
    
    Examples:
        >>> convert_to_kebab_case("HelloWorld")
        'hello-world'
        >>> convert_to_kebab_case("snake_case_string")
        'snake-case-string'
        >>> convert_to_kebab_case("camelCaseString")
        'camel-case-string'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to lowercase
    # Replace spaces, underscores, and handle camel case with a hyphen
    kebab_string = ''
    for i, char in enumerate(input_string):
        if i > 0 and char.isupper():
            kebab_string += '-'
        
        if char.isalnum():
            kebab_string += char.lower()
        elif char in [' ', '_']:
            kebab_string += '-'
    
    # Remove consecutive hyphens and trim leading/trailing hyphens
    while '--' in kebab_string:
        kebab_string = kebab_string.replace('--', '-')
    
    return kebab_string.strip('-')