def to_dot_case(input_string):
    """
    Convert a string to dot case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The input string converted to dot case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_dot_case("hello world")
        'hello.world'
        >>> to_dot_case("HelloWorld")
        'hello.world'
        >>> to_dot_case("hello_world")
        'hello.world'
        >>> to_dot_case("HELLO-WORLD")
        'hello.world'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase
    lowercase = input_string.lower()
    
    # Replace various separators with dots
    dot_case = lowercase.replace(' ', '.').replace('_', '.').replace('-', '.')
    
    # Remove consecutive dots
    while '..' in dot_case:
        dot_case = dot_case.replace('..', '.')
    
    # Remove leading and trailing dots
    dot_case = dot_case.strip('.')
    
    return dot_case