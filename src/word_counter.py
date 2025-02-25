def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input string to count words in.
    
    Returns:
        int: The number of words in the string.
    
    Notes:
    - Words are defined as sequences of non-whitespace characters
    - Multiple consecutive whitespaces are treated as a single separator
    - Empty string or string with only whitespaces returns 0
    """
    # Handle None or empty input
    if text is None:
        return 0
    
    # Strip leading and trailing whitespaces and split on whitespace
    words = text.strip().split()
    
    return len(words)