import re

def split_text_to_words(text):
    """
    Split text into words based on specific parsing rules.
    
    Args:
        text (str): Input text with no spaces
    
    Returns:
        list: List of words extracted from the text
    """
    if not text:
        return []
    
    # Regex explanation:
    # - Capture groups to preserve separators
    # - (?=[A-Z]) is a positive lookahead for capital letters
    # - Include punctuation (except quotes) as separators
    words = []
    current_word = text[0]
    
    for char in text[1:]:
        # Check if current character breaks a word
        if (char.isupper() and not current_word[-1].isupper()) or \
           (char in '.,;:!?-' and char != '"'):
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    
    words.append(current_word)
    return words