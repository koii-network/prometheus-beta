import re

def reverse_words_in_string(s):
    """
    Reverse the order of each word in a string while maintaining original capitalization and punctuation.
    
    Args:
        s (str): The input string to reverse words in.
    
    Returns:
        str: A string with words reversed, preserving original capitalization and punctuation.
    """
    # Split the string into words while preserving punctuation
    def split_with_punctuation(text):
        return re.findall(r'\b\w+\b|\W+', text)
    
    # Reverse a single word while preserving its original capitalization
    def reverse_word(word):
        # If the word is not alphabetic (e.g., punctuation), return it as-is
        if not word.isalpha():
            return word
        
        # Check original word's capitalization
        if word.istitle():
            return word.lower()[::-1].capitalize()
        elif word.isupper():
            return word[::-1]
        else:
            return word[::-1]
    
    # Split the string, reverse each word, then join back
    words = split_with_punctuation(s)
    reversed_words = [reverse_word(word) for word in words]
    return ''.join(reversed_words)