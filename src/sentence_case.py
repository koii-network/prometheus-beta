def convert_to_sentence_case(text: str) -> str:
    """
    Convert a string to sentence case.
    
    Sentence case capitalizes the first character of the string 
    and ensures the rest of the characters are lowercase.
    
    Args:
        text (str): The input string to convert to sentence case.
    
    Returns:
        str: The input string converted to sentence case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_sentence_case("HELLO WORLD")
        'Hello world'
        >>> convert_to_sentence_case("hello WORLD")
        'Hello world'
        >>> convert_to_sentence_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return text
    
    # Convert to sentence case: first char uppercase, rest lowercase
    return text[0].upper() + text[1:].lower()