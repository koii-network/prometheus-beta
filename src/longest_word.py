import re

def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): A string containing words to search through.
    
    Returns:
        str: The longest word in the sentence. 
             If multiple words have the same maximum length, returns the first one.
             If the sentence is empty, returns an empty string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Split the sentence into words, removing punctuation and extra whitespace
    words = re.findall(r'\b\w+\b', sentence)
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Find the longest word
    return max(words, key=len)