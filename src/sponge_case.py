def to_sponge_case(text):
    """
    Convert a string to alternating sponge case (SpOnGeBoB cAsE).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )