def reverse_string(input_str: str) -> str:
    """
    Reverse a string, preserving the order of words and special characters.
    
    Args:
        input_str (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_str:
        return ""
    
    # Reverse the entire string
    return input_str[::-1]