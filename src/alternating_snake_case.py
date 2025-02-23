def convert_to_alternating_snake_case(input_string: str) -> str:
    """
    Convert a given string to alternating snake case.
    
    Alternating snake case means:
    - Words are separated by underscores
    - Odd-indexed words are lowercase
    - Even-indexed words are UPPERCASE
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating snake case
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    
    Examples:
        >>> convert_to_alternating_snake_case("hello world")
        'hello_WORLD'
        >>> convert_to_alternating_snake_case("python is awesome")
        'python_IS_awesome'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string.strip():
        raise ValueError("Input string cannot be empty")
    
    # Split the input string into words
    words = input_string.split()
    
    # Convert words alternately
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even indices (0, 2, 4...) are lowercase
            converted_words.append(word.lower())
        else:
            # Odd indices (1, 3, 5...) are UPPERCASE
            converted_words.append(word.upper())
    
    # Join the words with underscores
    return '_'.join(converted_words)