def to_alternating_header_case(input_string: str) -> str:
    """
    Convert a string to alternating header case.
    
    This function takes a string and converts it to alternating header case,
    where words alternate between capitalized and a special alternating case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating header case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_header_case("hello world")
        'Hello wOrLd'
        >>> to_alternating_header_case("python programming")
        'Python pRoGrAmMiNg'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Strip extra whitespace and split into words
    words = input_string.strip().split()
    
    # Convert words to alternating case
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0-based) are capitalized
            converted_word = word.capitalize()
        else:
            # Odd index words alternate between lowercase and uppercase
            converted_word = ''.join(
                char.lower() if j % 2 == 1 else char.upper() 
                for j, char in enumerate(word)
            )
        converted_words.append(converted_word)
    
    # Join the words back together
    return ' '.join(converted_words)