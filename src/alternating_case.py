def to_alternating_sentence_case(text):
    """
    Convert a string to alternating sentence case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating sentence case.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return empty string
    if not text:
        return ""
    
    # Convert to alternating sentence case
    result = []
    for i, char in enumerate(text):
        # Alternate based on index, starting with uppercase
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)