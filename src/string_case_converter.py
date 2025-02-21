import re

def to_kebab_case(input_string):
    """
    Convert a string to kebab-case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to kebab-case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Replace non-alphanumeric characters with spaces
    # Convert to lowercase
    # Replace multiple spaces with a single space
    # Replace spaces with hyphens
    # Remove leading/trailing hyphens
    kebab_string = re.sub(r'\s+', '-', 
                          re.sub(r'[^a-z0-9\s]', '', 
                                 input_string.lower().strip())).strip('-')
    
    return kebab_string