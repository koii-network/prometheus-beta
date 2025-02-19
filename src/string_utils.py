def convert_to_constant_case(input_string: str) -> str:
    """
    Convert a given string to CONSTANT_CASE.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to CONSTANT_CASE.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_constant_case("hello world")
        'HELLO_WORLD'
        >>> convert_to_constant_case("camelCaseString")
        'CAMEL_CASE_STRING'
        >>> convert_to_constant_case("snake_case_string")
        'SNAKE_CASE_STRING'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace non-alphanumeric characters with underscores
    normalized = ''.join(
        '_' if not char.isalnum() else char 
        for char in input_string
    )
    
    # Convert the normalized string to uppercase and replace multiple underscores with a single underscore
    constant_case = '_'.join(
        word.upper() for word in normalized.split('_') 
        if word
    )
    
    return constant_case