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
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Strip leading and trailing whitespace and split on whitespace
    # Filter out empty strings to handle multiple consecutive whitespaces
    words = [word for word in text.strip().split() if word]
    
    return len(words)