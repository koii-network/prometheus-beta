def remove_duplicate_words(input_string):
    """
    Remove duplicate words from a given string, preserving the original order of first occurrence.
    
    Args:
        input_string (str): The input string to remove duplicate words from.
    
    Returns:
        str: A new string with duplicate words removed, keeping the first occurrence of each word.
    
    Examples:
        >>> remove_duplicate_words("hello hello world")
        'hello world'
        >>> remove_duplicate_words("the quick brown fox jumps the quick fox")
        'the quick brown fox jumps'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words, use a list to preserve order
    words = input_string.split()
    
    # Use a set to track seen words while preserving order
    unique_words = []
    seen_words = set()
    
    for word in words:
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return ' '.join(unique_words)