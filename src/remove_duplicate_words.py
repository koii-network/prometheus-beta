def remove_duplicate_words(input_string):
    """
    Remove duplicate words from a given string while preserving the original order.

    Args:
        input_string (str): The input string containing words to be deduplicated.

    Returns:
        str: A new string with duplicate words removed, maintaining the first occurrence order.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> remove_duplicate_words("hello world hello python world")
        'hello world python'
        >>> remove_duplicate_words("  a b c a b c  ")
        'a b c'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # Split the string into words, preserving whitespace
    words = input_string.split()

    # Use a list to maintain order while removing duplicates
    unique_words = []
    seen_words = set()

    for word in words:
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)

    # Join the unique words back into a string
    return ' '.join(unique_words)