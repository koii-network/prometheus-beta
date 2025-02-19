def convert_to_sentence_case(text: str) -> str:
    """
    Convert a string to sentence case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to sentence case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not text:
        return ""
    
    # Capitalize the first character and convert the rest to lowercase
    return text[0].upper() + text[1:].lower()