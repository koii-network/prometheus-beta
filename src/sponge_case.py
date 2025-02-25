def to_sponge_case(text: str) -> str:
    """
    Convert a string to sponge case (alternating upper and lower case).
    
    Args:
        text (str): The input string to be converted to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'HeLlO'
        >>> to_sponge_case("WORLD")
        'WoRlD'
        >>> to_sponge_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if not text:
        return ""
    
    # Convert to sponge case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )