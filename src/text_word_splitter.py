import re

def split_text_to_words(text):
    """
    Split text into words based on specific rules:
    1. Words are separated by capital letters or punctuation marks (excluding quotes)
    2. Punctuation marks at the end of words are included in the word
    3. Sequences of capital letters are treated as separate words
    4. Quotation marks do not break words
    
    Args:
        text (str): Input text without spaces
    
    Returns:
        list: List of words extracted from the text
    """
    if not text:
        return []
    
    # Regex pattern to split text:
    # - Split before capital letters (lookahead)
    # - Split on punctuation (except quotes)
    # - Preserve punctuation at end of words
    pattern = r'(?=[A-Z])|([^\w\s"\']+$|[^\w\s"\']+(?=[A-Z]))'
    
    # Split the text and filter out empty strings
    words = [word for word in re.split(pattern, text) if word]
    
    return words