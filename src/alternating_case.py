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
    
    # Track index separately to reset for each word
    result = []
    word_index = 0
    
    for char in text:
        if char.isspace():
            # Reset word index on spaces
            word_index = 0
            result.append(char)
        else:
            # Apply alternating case based on word index
            result.append(
                char.upper() if word_index % 2 == 0 else char.lower()
            )
            word_index += 1
    
    return ''.join(result)