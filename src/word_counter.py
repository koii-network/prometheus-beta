def count_words(text):
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input text to count words from.
    
    Returns:
        int: The number of words in the text.
    
    Notes:
        - Words are defined as sequences of non-whitespace characters
        - Empty string or None returns 0
        - Handles multiple consecutive whitespaces
    """
    if text is None:
        return 0
    
    # Strip leading/trailing whitespace and split on whitespace
    words = text.strip().split()
    return len(words)