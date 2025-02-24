import re

def reverse_words_in_string(s):
    """
    Reverse the order of each word in the string while maintaining 
    original capitalization and punctuation.
    
    Args:
        s (str): Input string to be processed
    
    Returns:
        str: String with words reversed
    """
    # Handle empty string case
    if not s:
        return s
    
    # Split the string into words while preserving punctuation and whitespace
    def split_with_punctuation(text):
        return re.findall(r'\S+|\s+', text)
    
    # Reverse individual words while preserving case
    def reverse_word(word):
        # If the word is just whitespace or punctuation, return as-is
        if not re.match(r'\w', word):
            return word
        
        # Separate letters from punctuation
        letters = re.findall(r'\w', word)
        punctuation = re.findall(r'\W', word)
        
        # Reverse only the letters
        reversed_letters = list(reversed(letters))
        
        # Restore original capitalization
        if word[0].isupper():
            reversed_letters[0] = reversed_letters[0].upper()
        
        # Combine reversed letters with original punctuation
        result = []
        letter_index = 0
        punct_index = 0
        
        for char in word:
            if re.match(r'\w', char):
                result.append(reversed_letters[letter_index])
                letter_index += 1
            else:
                result.append(punctuation[punct_index])
                punct_index += 1
        
        return ''.join(result)
    
    # Split and process the words
    words = split_with_punctuation(s)
    reversed_words = [reverse_word(word) for word in words]
    
    return ''.join(reversed_words)