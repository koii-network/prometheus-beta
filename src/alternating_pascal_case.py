def to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: A string in alternating Pascal case.
    
    Examples:
        >>> to_alternating_pascal_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_pascal_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    if not input_string:
        return ""
    
    words = input_string.split()
    alternating_words = []
    
    for word in words:
        alternating_word = ''.join(
            char.upper() if idx % 2 == 0 else char.lower() 
            for idx, char in enumerate(word)
        )
        alternating_words.append(alternating_word)
    
    return ' '.join(alternating_words)