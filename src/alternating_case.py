def convert_to_alternating_lowercase(input_string):
    """
    Convert a string to alternating lowercase.

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A string with alternating lowercase characters.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not input_string:
        return ""
    
    # Convert to alternating lowercase
    return ''.join(
        char.lower() if idx % 2 == 0 else char.upper() 
        for idx, char in enumerate(input_string)
    ).upper()