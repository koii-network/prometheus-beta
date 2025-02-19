import re

def convert_to_constant_case(input_string):
    """
    Convert a string to constant case (ALL_UPPERCASE_WITH_UNDERSCORES).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to constant case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Remove leading/trailing whitespaces
    input_string = input_string.strip()
    
    # Handle camelCase and PascalCase by inserting underscores
    # Uses a regex that matches a lowercase letter followed by an uppercase letter
    input_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_string)
    
    # Replace various separators with underscores
    cleaned_string = input_string.replace('-', '_').replace(' ', '_')
    
    # Convert to uppercase
    constant_case = cleaned_string.upper()
    
    # Remove multiple consecutive underscores
    while '__' in constant_case:
        constant_case = constant_case.replace('__', '_')
    
    return constant_case