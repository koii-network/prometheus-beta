def convert_to_path_case(input_string):
    """
    Convert a string to path case.
    
    Path case is a string where:
    - All characters are lowercase
    - Spaces, underscores, and multiple spaces are replaced with a single hyphen
    - Removes leading and trailing whitespaces
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to path case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase
    converted = input_string.lower()
    
    # Replace multiple spaces, underscores with a single hyphen
    converted = converted.replace('_', '-')
    while '  ' in converted:
        converted = converted.replace('  ', ' ')
    
    # Replace remaining spaces with hyphens
    converted = converted.replace(' ', '-')
    
    # Remove leading and trailing hyphens
    converted = converted.strip('-')
    
    return converted