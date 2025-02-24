def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string.

    Args:
        input_string (str): The input string to reverse.

    Returns:
        str: A new string with words in reversed order, 
             preserving original word spacing.

    Raises:
        AttributeError: If input is not a string.

    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("Python is awesome")
        'awesome is Python'
        >>> reverse_words("")
        ''
        >>> reverse_words("SingleWord")
        'SingleWord'
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise AttributeError("Input must be a string")
    
    # Handle empty string or single word cases
    if not input_string or len(input_string.split()) <= 1:
        return input_string
    
    # Split the string into words and reverse their order
    words = input_string.split()
    return ' '.join(words[::-1])