import re

def to_snake_case(input_string: str) -> str:
    """
    Convert a given string to snake_case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The converted string in snake_case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_snake_case("HelloWorld")
        'hello_world'
        >>> to_snake_case("snake_case")
        'snake_case'
        >>> to_snake_case("camelCase")
        'camel_case'
        >>> to_snake_case("PascalCase")
        'pascal_case'
        >>> to_snake_case("mixed Case")
        'mixed_case'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace any non-alphanumeric characters with a single space
    # This helps handle mixed delimiter inputs
    cleaned = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Replace camelCase and PascalCase with snake_case
    # First, insert underscore before any uppercase letter 
    # that is preceded by a lowercase letter or number
    step1 = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', cleaned)
    
    # Convert to lowercase and replace remaining spaces with underscores
    snake_case = re.sub(r'\s+', '_', step1).lower()
    
    # Remove trailing underscore if present
    snake_case = snake_case.rstrip('_')
    
    return snake_case