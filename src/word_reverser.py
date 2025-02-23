def reverse_words(input_string):
    """
    Reverse the order of words in a given string.
    
    Args:
        input_string (str): The input string to reverse.
    
    Returns:
        str: A string with words in reverse order, handling multiple spaces and non-alphabetic characters.
    """
    # Remove extra spaces and split the string into words
    words = input_string.strip().split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words with a single space
    return ' '.join(reversed_words)