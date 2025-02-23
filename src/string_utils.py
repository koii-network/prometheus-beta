import re

def to_kebab_case(input_string: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Handles various input formats including:
    - Camel Case
    - Snake Case
    - Space-separated words
    - Mixed case strings
    
    Args:
        input_string (str): The input string to convert to kebab-case
    
    Returns:
        str: The input string converted to kebab-case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_kebab_case("HelloWorld")
        'hello-world'
        >>> to_kebab_case("hello_world")
        'hello-world'
        >>> to_kebab_case("Hello World")
        'hello-world'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace non-alphanumeric characters with a single space
    # This handles mixed separators and special characters
    cleaned = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Split the string, convert to lowercase, and join with hyphens
    # Use regex to split on capital letters for camel case
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', cleaned)
    
    # Convert to lowercase and join with hyphens
    return '-'.join(word.lower() for word in words)