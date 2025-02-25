def to_sponge_case(text: str) -> str:
    """
    Convert a string to sponge case (alternating uppercase and lowercase).
    
    Args:
        text (str): The input string to convert to sponge case.
    
    Returns:
        str: The input string converted to sponge case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello world")
        'HeLlO wOrLd'
        >>> to_sponge_case("")
        ''
        >>> to_sponge_case("a")
        'A'
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Empty string case
    if not text:
        return text
    
    # Convert to sponge case, preserving original spacing
    result = []
    count = 0
    for char in text:
        if char.isalpha():
            result.append(char.upper() if count % 2 == 0 else char.lower())
            count += 1
        else:
            result.append(char)
    
    return ''.join(result)