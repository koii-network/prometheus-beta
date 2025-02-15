def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input string to count words from.
    
    Returns:
        int: The number of words in the string.
    
    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("  Multiple   spaces   between words  ")
        3
        >>> count_words("")
        0
    """
    # Remove leading and trailing whitespace and split on whitespace
    # Using split() without arguments handles multiple consecutive whitespace characters
    if not text or not text.strip():
        return 0
    
    return len(text.strip().split())