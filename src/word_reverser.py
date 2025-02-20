def reverse_words_and_characters(input_string):
    """
    Reverse the order of words in a string and reverse the characters of each word.
    
    Args:
        input_string (str): The input string to be transformed
    
    Returns:
        str: A new string with words and characters reversed
    
    Examples:
        >>> reverse_words_and_characters("Hello World")
        "dlroW olleH"
        >>> reverse_words_and_characters("Python is awesome")
        "emosewa si nohtyP"
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty or just whitespace, return as is
    if not input_string.strip():
        return input_string
    
    # Split the string into words, reverse each word's characters, then reverse word order
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words[::-1])