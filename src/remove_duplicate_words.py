def remove_duplicate_words(sentence):
    """
    Remove duplicate words from a string while maintaining the original order.
    
    Args:
        sentence (str): The input string containing words.
    
    Returns:
        str: A new string with duplicate words removed, preserving original order.
    
    Examples:
        >>> remove_duplicate_words("the quick brown fox jumps the quick brown fox")
        'the quick brown fox jumps'
        >>> remove_duplicate_words("hello hello world world hello")
        'hello world'
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
    
    return ' '.join(unique_words)