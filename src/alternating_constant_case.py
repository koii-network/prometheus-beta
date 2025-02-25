def convert_to_alternating_constant_case(input_string):
    """
    Convert a string to alternating constant case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The input string converted to alternating constant case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    
    Examples:
        >>> convert_to_alternating_constant_case("hello world")
        'HELLO world'
        >>> convert_to_alternating_constant_case("python is awesome")
        'PYTHON is AWESOME'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string.strip():
        raise ValueError("Input string cannot be empty")
    
    # Split the input string into words and strip extra whitespace
    words = input_string.split()
    
    # Convert words to alternating constant case
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index words (0, 2, 4...) in UPPER CASE
            converted_words.append(word.upper())
        else:
            # Odd index words (1, 3, 5...) in lowercase
            converted_words.append(word.lower())
    
    # Join the words back together
    return ' '.join(converted_words)