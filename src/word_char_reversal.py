def reverse_words_and_chars(input_string):
    """
    Reverse the order of words in a string and also reverse the characters of each word.
    
    Args:
        input_string (str): The input string to be transformed
    
    Returns:
        str: A string with words in reverse order and each word's characters reversed
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return ""
    
    # Split the string into words, reverse the order, reverse each word's characters
    words = input_string.split()
    reversed_words = [word[::-1] for word in words[::-1]]
    
    return ' '.join(reversed_words)