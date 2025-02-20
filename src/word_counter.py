import re

def count_unique_words(text):
    """
    Count the number of unique words in a given text, 
    ignoring case and punctuation.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        int: Number of unique words
    """
    # Convert to lowercase and remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words and create a unique set
    unique_words = set(cleaned_text.split())
    
    return len(unique_words)