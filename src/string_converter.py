import re

def to_snake_case(input_string: str) -> str:
    """
    Convert a given string to snake_case.
    
    This function handles various input formats including:
    - Camel Case
    - Pascal Case
    - Kebab Case
    - Space-separated strings
    - Strings with mixed punctuation
    
    Args:
        input_string (str): The input string to convert to snake case
    
    Returns:
        str: The converted snake_case string
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_snake_case("HelloWorld")
        'hello_world'
        >>> to_snake_case("hello-world")
        'hello_world'
        >>> to_snake_case("Hello World")
        'hello_world'
        >>> to_snake_case("hello_world")
        'hello_world'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace any non-alphanumeric characters with a single space
    # This handles mixed punctuation and multiple separators
    cleaned_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Insert underscore before any uppercase letters 
    # and convert to lowercase, but only for non-first characters
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', cleaned_string)
    
    # Convert to lowercase and replace multiple spaces with single underscore
    snake_case = re.sub(r'\s+', '_', snake_case).lower()
    
    # Remove leading/trailing underscores
    return snake_case.strip('_')