def convert_to_header_case(input_string):
    """
    Convert a string to header case.
    
    Header case capitalizes the first letter of each word and removes spaces/separators.
    
    Args:
        input_string (str): The input string to be converted to header case.
    
    Returns:
        str: The converted string in header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_header_case("hello world")
        'HelloWorld'
        >>> convert_to_header_case("python_is_awesome")
        'PythonIsAwesome'
        >>> convert_to_header_case("convert-to-header-case")
        'ConvertToHeaderCase'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace common separators with a space
    normalized_string = input_string.replace('_', ' ').replace('-', ' ')
    
    # Split the string into words and capitalize each word
    words = [word.capitalize() for word in normalized_string.split()]
    
    # Join the words together without spaces
    return ''.join(words)