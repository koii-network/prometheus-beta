import re

def split_text_into_words(text):
    """
    Split text into words based on specific rules:
    1. Words are separated by capital letters or punctuation (excluding quotes)
    2. Punctuation marks are included at the end of words
    3. Sequences of capital letters are treated as separate words
    4. Quotation marks do not break words
    
    Args:
        text (str): Input text without spaces
    
    Returns:
        list: A list of words
    """
    if not text:
        return []
    
    # Regex pattern to split text based on the given rules
    # Positive lookbehind ensures punctuation is included with the preceding word
    # Handles capital letters and punctuation while preserving quoted sections
    pattern = r'(?<=[a-z0-9"])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|(?<=[a-zA-Z0-9"])(?=[.,;:!?])'
    
    # Split the text while preserving punctuation and handling capital letters
    words = re.split(pattern, text)
    
    # Remove any empty strings from the result
    words = [word for word in words if word]
    
    return words