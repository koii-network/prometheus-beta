def to_alternating_pascal_case(input_string):
    """
    Convert a string to alternating Pascal case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_pascal_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_pascal_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Convert each word to alternating case
    alternating_words = []
    for word in words:
        # Create alternating case word
        alternating_word = ''.join(
            char.upper() if i % 2 == 0 else char.lower() 
            for i, char in enumerate(word)
        )
        alternating_words.append(alternating_word)
    
    # Join the words back together
    return ' '.join(alternating_words)