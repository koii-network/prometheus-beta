def reverse_words_and_characters(input_string):
    """
    Reverses the order of words in a string and also reverses the characters of each word.
    
    Args:
        input_string (str): The input string to be transformed
    
    Returns:
        str: A string with words in reverse order and each word's characters reversed
    """
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Reverse the order of words and reverse characters in each word
    reversed_words = [word[::-1] for word in words[::-1]]
    
    # Join the reversed words back into a string
    return " ".join(reversed_words)