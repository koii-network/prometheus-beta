import re

def advanced_string_reversal(input_string):
    """
    Reverses a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromic substrings are left unchanged
    3. Words (letter-only substrings) are reversed
    
    Args:
        input_string (str): The input string to be processed
    
    Returns:
        str: The processed string with applied reversal rules
    """
    def is_palindrome(s):
        """Check if a substring is a palindrome"""
        return s == s[::-1]
    
    def is_word(s):
        """Check if a substring is composed of only letters"""
        return s.isalpha()
    
    def process_token(token):
        """Process each token based on the special rules"""
        if is_palindrome(token):
            return token
        elif is_word(token):
            return token[::-1]
        elif token.isdigit():
            return token[::-1]
        else:
            return token
    
    # Split the input string into tokens, preserving spaces and non-letter/non-digit characters
    tokens = re.findall(r'\b\w+\b|\W+', input_string)
    
    # Apply processing to each token
    processed_tokens = [process_token(token) for token in tokens]
    
    # Reconstruct the string
    return ''.join(processed_tokens)