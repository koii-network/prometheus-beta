def to_sponge_case(text):
    """
    Convert a string to alternating sponge case (randomly capitalized).
    
    Args:
        text (str): The input string to convert to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    import random
    
    return ''.join(
        char.upper() if random.random() > 0.5 else char.lower() 
        for char in text
    )