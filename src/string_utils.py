def to_sentence_case(text: str) -> str:
    """
    Convert a string to sentence case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to sentence case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not text:
        return text
    
    # Capitalize the first character and lowercase the rest
    return text[0].upper() + text[1:].lower()