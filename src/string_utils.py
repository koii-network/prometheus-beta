def to_title_case(input_string):
    """
    Convert a string to title case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to title case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the string into words and capitalize each word
    return ' '.join(word.capitalize() for word in input_string.split())