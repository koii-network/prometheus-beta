def to_sponge_case(text: str) -> str:
    """
    Convert a string to alternating sponge case (SpOnGeBoB cAsE).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating sponge case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_sponge_case("hello")
        'hElLo'
        >>> to_sponge_case("python")
        'pYtHoN'
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Convert to alternating case
    return ''.join(
        char.upper() if idx % 2 == 1 else char.lower() 
        for idx, char in enumerate(text)
    )