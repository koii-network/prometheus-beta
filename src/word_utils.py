def remove_duplicate_words(text: str) -> str:
    """
    Remove duplicate words from a string while maintaining the original order.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with duplicate words removed, preserving the first occurrence.

    Examples:
        >>> remove_duplicate_words("hello world hello python world")
        'hello world python'
        >>> remove_duplicate_words("the quick brown fox jumps the quick fox")
        'the quick brown fox jumps'
    """
    # Handle edge cases
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if not text:
        return ""
    
    # Split the string into words
    words = text.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    result = []
    
    for word in words:
        # Only add the word if it hasn't been seen before
        if word not in seen_words:
            result.append(word)
            seen_words.add(word)
    
    # Join the words back into a string
    return " ".join(result)