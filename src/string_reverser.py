import re

def reverse_string_with_rules(input_string):
    """
    Reverse a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes remain unchanged
    3. Words (letter sequences) are reversed

    Args:
        input_string (str): The input string to be processed

    Returns:
        str: The processed string with specified reversing rules
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        return input_string

    # Helper function to check if a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]
    
    # Split the string into tokens, including whole words and numbers
    tokens = re.findall(r'\b[a-zA-Z]+\b|\b\d+\b|[^\w\s]|\s+|.', input_string)
    
    # Process each token
    processed_tokens = []
    for token in tokens:
        if token.isdigit():
            # Reverse integers
            processed_tokens.append(token[::-1])
        elif token.isalpha():
            # Reverse words
            processed_tokens.append(token[::-1])
        elif is_palindrome(token):
            # Keep palindromes unchanged
            processed_tokens.append(token)
        else:
            # Keep other characters as they are
            processed_tokens.append(token)
    
    # Reconstruct the string
    return ''.join(processed_tokens)