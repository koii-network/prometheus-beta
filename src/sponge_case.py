def convert_to_sponge_case(text: str) -> str:
    """
    Convert a string to sponge case (alternating uppercase and lowercase).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to sponge case.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )