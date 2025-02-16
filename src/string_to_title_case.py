def convert_to_title_case(input_string: str) -> str:
    """
    Convert a given string to title case.
    
    Args:
        input_string (str): The input string to be converted to title case.
    
    Returns:
        str: The input string converted to title case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to title case
    return input_string.title()