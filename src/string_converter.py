def to_constant_case(input_string):
    """
    Convert a given string to constant case (UPPERCASE_WITH_UNDERSCORES).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to constant case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase first
    lowercase_str = input_string.lower()
    
    # Replace non-alphanumeric characters with underscores
    import re
    # Replace sequences of non-alphanumeric characters with a single underscore
    cleaned_str = re.sub(r'[^a-z0-9]+', '_', lowercase_str)
    
    # Remove leading or trailing underscores and convert to uppercase
    return cleaned_str.strip('_').upper()