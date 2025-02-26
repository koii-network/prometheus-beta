import random

def to_sponge_case(text):
    """
    Convert a string to sponge case (alternating uppercase and lowercase).
    
    Args:
        text (str): The input string to convert to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return ""
    
    sponge_text = ""
    for char in text:
        # Randomly decide to make the character upper or lower case
        sponge_text += char.upper() if random.choice([True, False]) else char.lower()
    
    return sponge_text