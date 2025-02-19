import re

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
    
    # Remove any non-alphanumeric characters and replace with underscore
    # Replace any camelCase or PascalCase with snake_case
    # Use regex to insert underscore before capital letters, convert to lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    
    # Convert to lowercase and replace multiple consecutive underscores with single underscore
    return re.sub(r'[^a-z0-9]+', '_', s2.lower()).strip('_')