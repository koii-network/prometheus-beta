def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input string to count words from.
    
    Returns:
        int: The number of words in the string.
    
    Notes:
        - Words are defined as sequences of non-whitespace characters
        - Handles multiple whitespace characters between words
        - Returns 0 for empty or whitespace-only strings
    """
    # Handle None or empty string
    if not text:
        return 0
    
    # Strip leading/trailing whitespace and split on whitespace
    words = text.strip().split()
    
    return len(words)