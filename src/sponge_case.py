def to_sponge_case(input_string: str) -> str:
    """
    Convert a string to alternating sponge case (MiXeD cApS).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating sponge case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_sponge_case("hello world")
        'hElLo WoRlD'
        >>> to_sponge_case("")
        ''
        >>> to_sponge_case("a")
        'A'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(input_string):
        # Alternate between uppercase and lowercase based on index
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
    
    return ''.join(result)