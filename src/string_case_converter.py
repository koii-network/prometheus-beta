def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HeLlO WoRlD'
        >>> convert_to_alternating_pascal_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Split the string and remove extra whitespace
    words = input_string.split()
    
    # Convert each word to alternating case
    alternating_words = []
    for word in words:
        # Convert to alternating case
        alternating_word = ''.join(
            char.upper() if idx % 2 == 0 else char.lower() 
            for idx, char in enumerate(word)
        )
        alternating_words.append(alternating_word)
    
    # Join the words back together
    return ' '.join(alternating_words)