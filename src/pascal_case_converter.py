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
    
    # Split a camelCase or mixed case string 
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', input_string)
    
    # Replace any remaining non-alphanumeric characters and split
    words = [re.sub(r'[^a-zA-Z0-9]', '', word) for word in words]
    
    # Remove empty strings and capitalize
    words = [word.capitalize() for word in words if word]
    
    return ''.join(words)