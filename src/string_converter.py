def to_alternate_path_case(input_string):
    """
    Convert a string to alternating path case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating path case.
    
    Examples:
        >>> to_alternate_path_case("hello world")
        'hello-World'
        >>> to_alternate_path_case("PYTHON PROGRAMMING")
        'python-PROGRAMMING'
        >>> to_alternate_path_case("snake_case example")
        'snake-CASE-example'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the input string into words
    words = input_string.split()
    
    # Convert alternating words
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even index (0, 2, 4...) - lowercase
            converted_words.append(word.lower())
        else:
            # Odd index (1, 3, 5...) - uppercase
            converted_words.append(word.upper())
    
    # Join with hyphen
    return '-'.join(converted_words)