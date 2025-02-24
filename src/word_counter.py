def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    A word is defined as a sequence of non-whitespace characters.
    
    Args:
        text (str): The input string to count words in.
    
    Returns:
        int: The number of words in the string.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("  Multiple   spaces   between words  ")
        3
        >>> count_words("")
        0
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Use a single split to handle multiple spaces
    words = [word for word in text.split() if word]
    
    return len(words)