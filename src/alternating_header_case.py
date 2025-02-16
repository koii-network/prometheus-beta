def to_alternating_header_case(text):
    """
    Convert a string to alternating header case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating header case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    capitalize_next = True
    
    for char in text:
        if char.isalpha():
            if capitalize_next:
                result.append(char.upper())
            else:
                result.append(char.lower())
            capitalize_next = not capitalize_next
        else:
            result.append(char)
    
    return ''.join(result)