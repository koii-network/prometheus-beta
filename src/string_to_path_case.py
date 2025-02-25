import re

def to_path_case(input_string: str) -> str:
    """
    Convert a given string to path case.
    
    Path case is a string representation where:
    - All characters are lowercase
    - Words are separated by forward slashes
    - Removes special characters and replaces spaces/non-alphanumeric chars with slashes
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to path case
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_path_case("Hello World")
        'hello/world'
        >>> to_path_case("Python_Programming Language")
        'python/programming/language'
        >>> to_path_case("123 Test Case!")
        '123/test/case'
    """
    # Type checking
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace underscores and multiple spaces with single spaces
    normalized = re.sub(r'[_\s]+', ' ', input_string)
    
    # Remove special characters
    cleaned = re.sub(r'[^a-zA-Z0-9 ]', '', normalized)
    
    # Split into words, separating numbers from letters
    words = re.findall(r'\d+|[a-zA-Z]+', cleaned.lower())
    
    # Return path case version
    return '/'.join(words)