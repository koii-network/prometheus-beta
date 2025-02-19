def remove_duplicate_words(input_string):
    """
    Remove duplicate words from a given string while preserving the original order.
    
    Args:
        input_string (str): The input string with potentially duplicate words
    
    Returns:
        str: A new string with duplicate words removed, keeping the first occurrence
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = input_string.split()
    
    # Use a list to preserve order and keep track of seen words
    unique_words = []
    seen = set()
    
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    
    # Join the unique words back into a string
    return ' '.join(unique_words)