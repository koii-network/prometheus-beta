def convert_to_sponge_case(text):
    """
    Convert a string to alternating SpOnGe CaSe.
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The string converted to alternating case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    result = []
    for i, char in enumerate(text):
        # Alternate uppercase and lowercase based on index
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    
    return ''.join(result)