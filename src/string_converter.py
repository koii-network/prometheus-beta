def to_header_case(input_string):
    """
    Convert a string to header case.
    
    Header case capitalizes the first letter of each word and removes spaces.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to header case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty or whitespace-only strings
    if not input_string.strip():
        return ""
    
    # Split the string by non-alphanumeric characters
    words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in input_string).split()
    
    # Capitalize each word and join
    return ''.join(word.capitalize() for word in words)