import random

def to_sponge_case(text):
    """
    Convert a string to sponge case (AlTeRnAtInG cAsE) with randomized capitalization.
    
    Args:
        text (str): The input string to convert to sponge case
    
    Returns:
        str: The input string converted to sponge case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in text
    )