import re

def to_pascal_case(input_string: str) -> str:
    """
    Convert a given string to Pascal case.
    
    Pascal case is a naming convention where the first letter of each word is capitalized,
    and there are no separators between words.
    
    Args:
        input_string (str): The input string to convert to Pascal case.
    
    Returns:
        str: The input string converted to Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_pascal_case("hello world")
        'HelloWorld'
        >>> to_pascal_case("hello_world")
        'HelloWorld'
        >>> to_pascal_case("hello-world")
        'HelloWorld'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If the input is empty, return an empty string
    if not input_string:
        return ""
    
    # Remove leading and trailing whitespace
    input_string = input_string.strip()
    
    # Replace non-alphanumeric characters with space
    input_string = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Split the string into words
    words = input_string.split()
    
    # Capitalize each word
    pascal_words = [word.capitalize() for word in words]
    
    return ''.join(pascal_words)