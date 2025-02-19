def lowercase_with_spaces(input_string: str) -> str:
    """
    Convert a string to lowercase, replacing non-alphanumeric characters with spaces.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The lowercase string with non-alphanumeric characters replaced by spaces.
    
    Examples:
        >>> lowercase_with_spaces("Hello World!")
        'hello world'
        >>> lowercase_with_spaces("Python_is-AWESOME")
        'python is awesome'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase and replace non-alphanumeric characters with spaces
    return ''.join(char.lower() if char.isalnum() else ' ' for char in input_string).strip()