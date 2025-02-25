import re

def to_kebab_case(input_string: str) -> str:
    """
    Convert a given string to kebab-case.
    
    Kebab case is a naming convention where words are lowercase and 
    separated by hyphens. This function handles various input formats.
    
    Args:
        input_string (str): The input string to convert to kebab case.
    
    Returns:
        str: The input string converted to kebab case.
    
    Raises:
        TypeError: If the input is not a string.
    
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
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Handle camel case by inserting spaces before capital letters
    # except for the first letter
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
    
    # Replace multiple types of word separators with a single space
    normalized = s2.replace('_', ' ').replace('-', ' ')
    
    # Split the string, convert to lowercase, and join with hyphens
    words = normalized.split()
    return '-'.join(word.lower() for word in words)