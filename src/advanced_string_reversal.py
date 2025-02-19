import re

def advanced_string_reversal(input_string):
    """
    Reverse a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes are left unchanged
    3. Words (composed of only letters) are reversed
    
    Args:
        input_string (str): The input string to be processed
    
    Returns:
        str: The processed string with special reversals
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    def reverse_word(word):
        """Reverse a word if it's not a palindrome."""
        return word if is_palindrome(word) else word[::-1]
    
    # Split the string while preserving delimiters
    tokens = re.findall(r'(\d+|[a-zA-Z]+|\s+|[^\w\s])', input_string)
    
    # Process each token
    processed_tokens = []
    for token in tokens:
        if token.isdigit():  # Integers are reversed separately as strings
            processed_tokens.append(token[::-1])
        elif token.isalpha():  # Words are reversed if not palindromes
            processed_tokens.append(reverse_word(token))
        else:  # Whitespace and punctuation remain unchanged
            processed_tokens.append(token)
    
    return ''.join(processed_tokens)