import re

def advanced_string_reversal(input_string):
    """
    Reverse a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes remain unchanged
    3. Words (letter-only substrings) are reversed

    Args:
        input_string (str): The input string to be processed

    Returns:
        str: The processed string with special reversal rules applied
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    def is_palindrome(s):
        """Check if a substring is a palindrome."""
        return s == s[::-1]
    
    def is_word(s):
        """Check if a substring is composed of only letters."""
        return s.isalpha()
    
    def reverse_part(part):
        """Reverse a part based on its characteristics."""
        # If it's a palindrome, return as-is
        if is_palindrome(part):
            return part
        
        # If it's a word, reverse it
        if is_word(part):
            return part[::-1]
        
        # If it's a number (or contains numbers), reverse it
        try:
            int(part)
            return part[::-1]
        except ValueError:
            return part

    # Split the string into parts (words, numbers, and other characters)
    parts = re.findall(r'\d+|[a-zA-Z]+|\W+', input_string)
    
    # Apply reversal to each part
    reversed_parts = [reverse_part(part) for part in parts]
    
    # Reconstruct the string
    return ''.join(reversed_parts)