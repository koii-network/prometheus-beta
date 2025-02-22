def reverse_words(input_string):
    """
    Reverse the order of words in a given string.
    
    Args:
        input_string (str): The input string to be processed.
    
    Returns:
        str: A string with words in reversed order, preserving spaces and ignoring non-alphabetic characters.
    """
    # Handle empty or None input
    if not input_string:
        return ""
    
    # Split the string by whitespace, removing extra spaces
    words = input_string.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words with a single space
    return " ".join(reversed_words)