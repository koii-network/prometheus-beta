import re

def count_unique_words(text):
    """
    Count the number of unique words in a given text, ignoring case and punctuation.
    
    Args:
        text (str): The input text to analyze
    
    Returns:
        int: Number of unique words in the text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', text)
    
    # Return count of unique words
    return len(set(words))