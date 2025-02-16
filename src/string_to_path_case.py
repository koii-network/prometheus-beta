import re

def convert_to_path_case(input_string: str) -> str:
    """
    Convert a given string to path case.
    
    Path case means:
    - Convert to lowercase
    - Replace spaces, underscores, and multiple consecutive separators with a single '/'
    - Remove leading and trailing separators
    - Trim multiple consecutive slashes to a single slash
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to path case
    
    Examples:
        >>> convert_to_path_case("Hello World")
        'hello/world'
        >>> convert_to_path_case("Some_Mixed Case String")
        'some/mixed/case/string'
        >>> convert_to_path_case("  extra   spaces  ")
        'extra/spaces'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Replace multiple types of separators with a slash
    path_string = re.sub(r'[_\s]+', '/', input_string)
    
    # Remove leading and trailing slashes
    path_string = path_string.strip('/')
    
    # Remove multiple consecutive slashes
    path_string = re.sub(r'/+', '/', path_string)
    
    return path_string