def convert_to_header_case(input_string: str) -> str:
    """
    Convert a string to header case.
    
    Header case capitalizes the first letter of each word, 
    removing any existing separators.
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to header case
    
    Examples:
        >>> convert_to_header_case("hello world")
        'HelloWorld'
        >>> convert_to_header_case("hello_world")
        'HelloWorld'
        >>> convert_to_header_case("hello-world")
        'HelloWorld'
        >>> convert_to_header_case("hello world_test-case")
        'HelloWorldTestCase'
    """
    # Handle None or empty string input
    if input_string is None:
        return ""
    
    # Replace common separators with space
    cleaned_string = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string, capitalize each word, and join
    return ''.join(word.capitalize() for word in cleaned_string.split())