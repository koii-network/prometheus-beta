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
    
    # Handle camel case by inserting dots
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1.\2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1.\2', s1)
    
    # Convert to lowercase and replace non-alphanumeric characters with dots
    s3 = re.sub(r'[^a-zA-Z0-9]+', '.', s2)
    
    # Insert dots between letters and numbers
    s4 = re.sub(r'([a-z])(\d)', r'\1.\2', s3)
    s5 = re.sub(r'(\d)([a-z])', r'\1.\2', s4)
    
    # Convert to lowercase and remove consecutive dots
    result = re.sub(r'\.+', '.', s5.lower()).strip('.')
    
    return result