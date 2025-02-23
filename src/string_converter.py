import re

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
    
    # Replace non-alphanumeric characters with spaces
    input_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Insert space before capital letters 
    # and split the string into words
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', input_string)
    
    # Convert to uppercase and join with underscores
    return '_'.join(word.upper() for word in words)