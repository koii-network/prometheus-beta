def alternating_sentence_case(text):
    """
    Convert a string to alternating sentence case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string with alternating uppercase and lowercase characters.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If empty string, return empty string
    if not text:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)