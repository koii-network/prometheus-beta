def count_words(text: str) -> int:
    """
    Count the number of words in a given string.
    
    Args:
        text (str): The input text to count words from.
    
    Returns:
        int: The number of words in the text.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Strip leading/trailing whitespace and split on whitespace
    # This handles multiple whitespace characters and trims excess spaces
    words = text.strip().split()
    
    return len(words)