def convert_to_uppercase_with_spaces(input_string):
    """
    Convert a string to uppercase with spaces between words.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string converted to uppercase with spaces added.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Remove existing spaces and convert to uppercase with spaces
    converted = ' '.join(input_string.replace(' ', '').upper())
    
    return converted