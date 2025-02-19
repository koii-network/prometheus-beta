def convert_to_dot_case(input_string):
    """
    Convert a string to dot case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to dot case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Replace non-alphanumeric characters with dots
    import re
    return re.sub(r'[^a-z0-9]+', '.', input_string)