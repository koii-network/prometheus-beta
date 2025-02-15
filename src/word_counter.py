def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input string to count words from.
    
    Returns:
        int: The number of words in the string.
    
    Notes:
        - Words are defined as sequences of non-whitespace characters.
        - Multiple consecutive whitespace characters are treated as a single separator.
        - Empty string or string with only whitespace returns 0.
    """
    if not text or text.isspace():
        return 0
    
    # Split the string by whitespace and count non-empty elements
    return len([word for word in text.split() if word])