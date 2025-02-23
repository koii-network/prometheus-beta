def remove_duplicate_words(sentence):
    """
    Remove duplicate words from a string while maintaining the original order.
    
    Args:
        sentence (str): Input string containing words
    
    Returns:
        str: String with duplicate words removed, preserving original order
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Split the sentence into words
    words = sentence.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    unique_words = []
    
    for word in words:
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a sentence
    return ' '.join(unique_words)