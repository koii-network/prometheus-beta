import re

def complex_string_reversal(input_string):
    """
    Reverses a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes are left unchanged
    3. Words (letter-only substrings) are reversed
    
    Args:
        input_string (str): The input string to be processed
    
    Returns:
        str: The processed string with special reversals
    """
    def is_palindrome(s):
        """Check if a substring is a palindrome."""
        return s == s[::-1]
    
    def is_word(s):
        """Check if a substring is composed of only letters."""
        return s.isalpha()
    
    def reverse_substring(s):
        """Reverse a substring based on its type."""
        if is_palindrome(s) or not is_word(s):
            return s
        return s[::-1]
    
    # Split the string into meaningful chunks
    chunks = re.findall(r'\d+|[a-zA-Z]+|\W+', input_string)
    
    # Process each chunk
    reversed_chunks = [reverse_substring(chunk) for chunk in chunks]
    
    # Reconstruct the string
    return ''.join(reversed_chunks)