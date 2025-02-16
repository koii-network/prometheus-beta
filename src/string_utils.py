def replace_spaces_with_underscores(text: str) -> str:
    """
    Replace all spaces in a given string with underscores.
    
    Args:
        text (str): The input string to modify.
    
    Returns:
        str: A new string with spaces replaced by underscores.
    
    Examples:
        >>> replace_spaces_with_underscores("hello world")
        'hello_world'
        >>> replace_spaces_with_underscores("  multiple   spaces  ")
        '__multiple___spaces__'
        >>> replace_spaces_with_underscores("")
        ''
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return text.replace(" ", "_")