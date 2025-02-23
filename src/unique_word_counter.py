import re

def count_unique_words(text):
    """
    Count the number of unique words in a given string, 
    ignoring case and punctuation.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        int: Number of unique words
    """
    # Handle None or empty string input
    if not text:
        return 0
    
    # Convert to lowercase and remove punctuation
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words and remove any empty strings
    words = [word for word in cleaned_text.split() if word]
    
    # Return count of unique words
    return len(set(words))