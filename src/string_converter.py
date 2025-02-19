import re

def to_constant_case(input_string):
    """
    Convert a string to constant case (ALL_UPPERCASE_WITH_UNDERSCORES).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to constant case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace non-alphanumeric characters with underscores
    # Remove leading/trailing non-alphanumeric characters
    # Convert to uppercase
    # Replace multiple consecutive underscores with a single underscore
    cleaned = re.sub(r'[^a-zA-Z0-9]+', '_', input_string)
    cleaned = cleaned.strip('_')
    constant_case = cleaned.upper()
    constant_case = re.sub(r'_+', '_', constant_case)
    
    return constant_case