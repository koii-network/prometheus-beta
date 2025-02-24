def remove_duplicate_words(input_string: str) -> str:
    """
    Remove duplicate words from a given string while preserving the original order of first occurrence.

    Args:
        input_string (str): The input string containing words to be deduplicated.

    Returns:
        str: A new string with duplicate words removed, keeping the first occurrence of each word.

    Examples:
        >>> remove_duplicate_words("hello world hello python world")
        'hello world python'
        >>> remove_duplicate_words("the quick brown fox jumps the quick fox")
        'the quick brown fox jumps'
    """
    # Handle edge cases
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return ""
    
    # Split the string into words and remove duplicates while preserving order
    seen_words = set()
    unique_words = []
    
    for word in input_string.split():
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return " ".join(unique_words)