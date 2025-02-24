def reverse_words_and_chars(input_string):
    """
    Reverse the order of words in a string and the characters within each word.
    
    Args:
        input_string (str): The input string to be reversed.
    
    Returns:
        str: A string with words in reverse order and each word's characters reversed.
    
    Examples:
        >>> reverse_words_and_chars("Hello World")
        "dlroW olleH"
        >>> reverse_words_and_chars("Python is awesome")
        "emosewa si nohtyP"
        >>> reverse_words_and_chars("")
        ""
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Reverse each word and then reverse the order of words
    reversed_words = [word[::-1] for word in words][::-1]
    
    # Join the reversed words back into a string
    return " ".join(reversed_words)