def to_alternating_case(text):
    """
    Convert a string to alternating case (SwApCaSe).

    Args:
        text (str): The input string to convert.

    Returns:
        str: The input string converted to alternating case.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> to_alternating_case("hello")
        'HeLlO'
        >>> to_alternating_case("WORLD")
        'WoRlD'
        >>> to_alternating_case("")
        ''
    """
    # Validate input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to alternating case
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower() 
        for i, char in enumerate(text)
    )