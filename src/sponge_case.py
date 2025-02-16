def to_sponge_case(text: str) -> str:
    """
    Convert a string to alternating sponge case (MiXeD cAsE).
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating sponge case.
    
    Examples:
        >>> to_sponge_case("hello world")
        'hElLo WoRlD'
        >>> to_sponge_case("python")
        'pYtHoN'
        >>> to_sponge_case("")
        ''
    """
    if not text:
        return text
    
    return ''.join(
        char.upper() if idx % 2 == 1 else char.lower() 
        for idx, char in enumerate(text)
    )