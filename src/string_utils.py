def replace_spaces_with_underscores(input_string: str) -> str:
    """
    Replace all spaces in a given string with underscores.
    
    Args:
        input_string (str): The original string containing spaces.
    
    Returns:
        str: A new string with spaces replaced by underscores.
    
    Examples:
        >>> replace_spaces_with_underscores("hello world")
        'hello_world'
        >>> replace_spaces_with_underscores("  extra  spaces  ")
        '__extra__spaces__'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    return input_string.replace(" ", "_")