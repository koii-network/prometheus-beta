def to_dot_case(input_string):
    """
    Convert a string to dot case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The dot case representation of the input string.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Replace multiple types of separators with a single dot
    import re
    # Replace non-alphanumeric characters (except dots) with dots
    converted = re.sub(r'[^a-z0-9]+', '.', input_string)
    
    # Remove consecutive dots
    converted = re.sub(r'\.+', '.', converted)
    
    # Remove leading or trailing dots
    converted = converted.strip('.')
    
    return converted