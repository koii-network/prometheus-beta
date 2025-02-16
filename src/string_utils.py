import re

def convert_to_snake_case(text: str) -> str:
    """
    Convert a given string to snake_case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The converted string in snake_case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Remove any non-alphanumeric characters
    # Replace spaces, camelCase, and PascalCase with underscores
    # Convert to lowercase
    # Remove leading/trailing underscores
    # Replace multiple consecutive underscores with a single underscore
    # Convert to lowercase
    snake_case = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
    snake_case = re.sub(r'[^a-zA-Z0-9]+', '_', snake_case)
    snake_case = snake_case.lower().strip('_')
    snake_case = re.sub(r'_+', '_', snake_case)
    
    return snake_case