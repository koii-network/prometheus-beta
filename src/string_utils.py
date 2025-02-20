def remove_duplicate_words(text):
    """
    Remove duplicate words from a string while maintaining the original order.
    
    Args:
        text (str): Input string containing words
    
    Returns:
        str: String with duplicate words removed, preserving first occurrence
    """
    # Split the string into words
    words = text.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    unique_words = []
    
    for word in words:
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return ' '.join(unique_words)