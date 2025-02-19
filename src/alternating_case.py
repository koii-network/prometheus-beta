def to_alternating_sentence_case(text):
    """
    Convert a string to alternating sentence case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating capitalization for each character.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)