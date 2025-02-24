def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input string to count words in.
    
    Returns:
        int: The number of words in the string.
    
    Notes:
        - Words are defined as sequences of non-whitespace characters.
        - Handles empty strings, strings with only whitespace, and multiple whitespaces.
    
    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("   Multiple   spaces   ")
        2
        >>> count_words("")
        0
    """
    # Handle None or non-string input
    if text is None:
        return 0
    
    # Convert to string and strip leading/trailing whitespace
    text = str(text).strip()
    
    # If string is empty after stripping, return 0
    if not text:
        return 0
    
    # Split by whitespace and count non-empty words
    return len([word for word in text.split() if word])