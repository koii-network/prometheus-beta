def convert_to_alternating_sentence_case(text):
    """
    Convert a string to alternating sentence case.
    
    In alternating sentence case, each character alternates between uppercase 
    and lowercase, starting with uppercase for the first character.
    
    Args:
        text (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating sentence case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_alternating_sentence_case("hello world")
        'HeLlO WoRlD'
        >>> convert_to_alternating_sentence_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Convert to alternating case
    return ''.join(
        char.upper() if idx % 2 == 0 else char.lower() 
        for idx, char in enumerate(text)
    )