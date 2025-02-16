def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input string to count words from.
    
    Returns:
        int: The number of words in the string.
    
    Notes:
    - Words are separated by whitespace (spaces, tabs, newlines)
    - Empty string returns 0
    - Strips leading and trailing whitespace before counting
    """
    # If input is None or not a string, raise TypeError
    if text is None:
        raise TypeError("Input must be a string")
    
    # Strip leading and trailing whitespace and split on whitespace
    # Filter out empty strings to handle multiple consecutive spaces
    words = [word for word in text.strip().split() if word]
    
    return len(words)