def remove_duplicate_words(input_string):
    """
    Remove duplicate words from a given string while preserving the original order.
    
    Args:
        input_string (str): The input string containing words.
    
    Returns:
        str: A new string with duplicate words removed, maintaining the first occurrence order.
    
    Examples:
        >>> remove_duplicate_words("hello world hello python world")
        'hello world python'
        >>> remove_duplicate_words("the quick brown fox jumps the quick fox")
        'the quick brown fox jumps'
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = input_string.split()
    
    # Use a dictionary to preserve order and track unique words
    unique_words = []
    seen = set()
    
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Join the unique words back into a string
    return ' '.join(unique_words)