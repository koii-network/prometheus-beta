def to_alternating_sentence_case(text):
    """
    Convert a string to alternating sentence case.
    
    Alternates between uppercase and lowercase letters, starting with uppercase.
    Preserves non-alphabetic characters and spaces.
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The string converted to alternating sentence case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    uppercase = True
    
    for char in text:
        if char.isalpha():
            if uppercase:
                result.append(char.upper())
            else:
                result.append(char.lower())
            uppercase = not uppercase
        else:
            result.append(char)
    
    return ''.join(result)