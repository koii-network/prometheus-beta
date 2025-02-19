import re

def advanced_string_reversal(input_string):
    """
    Reverses a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes are left unchanged
    3. Words (letter-only substrings) are reversed
    
    Args:
        input_string (str): The input string to be reversed
    
    Returns:
        str: The reversed string with special rules applied
    """
    # Helper function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]
    
    # Helper function to check if a string is a word (only letters)
    def is_word(s):
        return s.isalpha()
    
    # Helper function to reverse a substring
    def reverse_substring(s):
        if is_palindrome(s):
            return s
        if is_word(s):
            return s[::-1]
        if s.isdigit():
            return s[::-1]
        return s
    
    # Split the string into tokens (words, numbers, and other characters)
    tokens = re.findall(r'\w+|\W+', input_string)
    
    # Apply reversal rules to each token
    reversed_tokens = [reverse_substring(token) for token in tokens]
    
    # Reconstruct the string
    return ''.join(reversed_tokens)