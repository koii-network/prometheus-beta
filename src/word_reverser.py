import re

def reverse_words_in_string(s):
    """
    Reverse the order of each word in a string while maintaining 
    original capitalization and punctuation.
    
    Args:
        s (str): The input string to be processed
    
    Returns:
        str: String with words reversed, preserving capitalization and punctuation
    """
    # If string is empty or None, return as is
    if not s:
        return s
    
    # Split the string into words, preserving punctuation and whitespace
    def split_with_delimiters(text):
        return re.findall(r'\S+|\s+', text)
    
    # Reverse each word while maintaining its original capitalization
    def reverse_word(word):
        # Skip whitespace or punctuation
        if re.match(r'\s+|\W+', word):
            return word
        
        # Determine original capitalization
        is_first_upper = word[0].isupper()
        is_all_upper = word.isupper()
        
        # Reverse the word
        reversed_word = word[::-1]
        
        # Restore original capitalization
        if is_all_upper:
            return reversed_word.upper()
        elif is_first_upper:
            return reversed_word.capitalize()
        else:
            return reversed_word
    
    # Apply word reversal to the entire string
    words = split_with_delimiters(s)
    reversed_words = [reverse_word(word) for word in words]
    return ''.join(reversed_words)