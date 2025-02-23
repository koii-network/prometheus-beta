def convert_to_alternating_lower(input_string):
    """
    Convert a string to alternating lowercase.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string with alternating lowercase characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating lowercase
    return ''.join(char.lower() if i % 2 == 0 else char for i, char in enumerate(input_string))