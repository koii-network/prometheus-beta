def convert_to_snake_case(input_string):
    """
    Convert a given string to snake_case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to snake_case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase
    snake_case = input_string.lower()
    
    # Replace non-alphanumeric characters with underscores
    import re
    snake_case = re.sub(r'[^a-z0-9]+', '_', snake_case)
    
    # Remove leading and trailing underscores
    snake_case = snake_case.strip('_')
    
    return snake_case