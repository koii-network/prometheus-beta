def reverse_words_and_chars(input_string: str) -> str:
    """
    Reverse the order of words in a string and the characters within each word.
    
    Args:
        input_string (str): The input string to be transformed.
    
    Returns:
        str: A string with words in reverse order and each word's characters reversed.
    
    Examples:
        >>> reverse_words_and_chars("Hello World")
        'dlroW olleH'
        >>> reverse_words_and_chars("Python is awesome")
        'emosewa si nohtyP'
    
    Handles edge cases:
    - Empty string
    - Single word
    - Multiple words with varying lengths
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, reverse the list, then reverse chars in each word
    reversed_words = [word[::-1] for word in input_string.split()[::-1]]
    
    # Join the reversed words back into a string
    return " ".join(reversed_words)