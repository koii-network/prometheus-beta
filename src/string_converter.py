def to_constant_case(input_string):
    """
    Convert a given string to constant case (UPPER_SNAKE_CASE).
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to constant case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # Replace multiple consecutive non-alphanumeric characters with a single underscore
    import re
    
    # First, split camel case words
    camel_split = re.sub(r'([a-z])([A-Z])', r'\1_\2', input_string)
    
    # Replace non-alphanumeric characters with underscores
    cleaned_string = re.sub(r'[^a-zA-Z0-9]+', '_', camel_split)
    
    # Convert to uppercase and remove leading/trailing underscores
    constant_case = cleaned_string.upper().strip('_')
    
    return constant_case