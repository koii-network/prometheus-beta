def to_snake_case(input_string):
    """
    Convert a given string to snake_case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to snake_case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to lowercase and replace non-alphanumeric characters with underscores
    snake_case = input_string.lower()
    
    # Replace spaces, hyphens, and mixed case with underscores
    snake_case = ''.join(['_' if not c.isalnum() or c.isupper() else c for c in snake_case])
    
    # Remove leading and trailing underscores
    snake_case = snake_case.strip('_')
    
    # Replace multiple consecutive underscores with a single underscore
    import re
    snake_case = re.sub(r'_+', '_', snake_case)
    
    return snake_case