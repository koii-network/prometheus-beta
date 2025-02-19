def convert_to_dot_case(input_string: str) -> str:
    """
    Convert a given string to dot case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The input string converted to dot case.
    
    Examples:
        >>> convert_to_dot_case('hello world')
        'hello.world'
        >>> convert_to_dot_case('HelloWorld')
        'hello.world'
        >>> convert_to_dot_case('hello_world')
        'hello.world'
    """
    # Handle None or empty string
    if input_string is None:
        return ''
    
    # Convert to lowercase
    lowercase_str = input_string.lower()
    
    # Replace various separators with dots
    dot_case_str = lowercase_str.replace(' ', '.').replace('_', '.').replace('-', '.')
    
    # Remove multiple consecutive dots
    while '..' in dot_case_str:
        dot_case_str = dot_case_str.replace('..', '.')
    
    # Strip leading and trailing dots
    return dot_case_str.strip('.')