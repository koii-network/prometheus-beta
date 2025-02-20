def remove_duplicate_words(text):
    """
    Remove duplicate words from a string while maintaining the original order.
    
    Args:
        text (str): Input string with words to be processed
    
    Returns:
        str: A new string with duplicate words removed, preserving original order
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words, keeping track of seen words
    seen_words = set()
    result = []
    
    for word in text.split():
        # Only add the word if it hasn't been seen before
        if word not in seen_words:
            result.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return ' '.join(result)