import re

def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string.
    
    Args:
        input_string (str): The input string to reverse
    
    Returns:
        str: A string with words in reversed order, handling multiple spaces 
             and ignoring non-alphabetic characters
    """
    # Remove punctuation, strip whitespace, and split on multiple whitespace characters
    cleaned_string = re.sub(r'[^\w\s]', '', input_string)
    words = cleaned_string.strip().split()
    
    # Reverse the list of words and join back with a single space
    return ' '.join(words[::-1])