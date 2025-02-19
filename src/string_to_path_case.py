def string_to_path_case(input_string):
    """
    Convert a string to path case (lowercase with hyphens).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to path case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace non-alphanumeric characters with hyphens
    path_case = ''.join(char.lower() if char.isalnum() else '-' for char in input_string)
    
    # Remove consecutive hyphens
    while '--' in path_case:
        path_case = path_case.replace('--', '-')
    
    # Remove leading and trailing hyphens
    path_case = path_case.strip('-')
    
    return path_case