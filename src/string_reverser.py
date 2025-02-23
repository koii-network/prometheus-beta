def reverse_string_with_rules(input_string):
    """
    Reverse a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes are left unchanged
    3. Words (letter-only substrings) are reversed
    
    Args:
        input_string (str): The input string to be processed
    
    Returns:
        str: The processed string according to the specified rules
    
    Raises:
        TypeError: If input is not a string
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    def is_word(s):
        """Check if a string contains only letters."""
        return s.isalpha()
    
    def split_string(s):
        """
        Split the string into tokens based on non-letter characters.
        Tokens can be integers, words, or other characters.
        """
        tokens = []
        current_token = ""
        current_type = None
        
        for char in s:
            # Determine current character type
            if char.isdigit():
                char_type = 'digit'
            elif char.isalpha():
                char_type = 'letter'
            else:
                char_type = 'other'
            
            # If type changes, add previous token and start new one
            if current_type is not None and current_type != char_type:
                tokens.append(current_token)
                current_token = char
                current_type = char_type
            else:
                current_token += char
                current_type = char_type
        
        # Add last token
        if current_token:
            tokens.append(current_token)
        
        return tokens
    
    # Process tokens
    tokens = split_string(input_string)
    processed_tokens = []
    
    for token in tokens:
        # Preserve palindromes
        if is_palindrome(token):
            processed_tokens.append(token)
        # Reverse words
        elif is_word(token):
            processed_tokens.append(token[::-1])
        # Reverse numeric tokens
        elif token.isdigit():
            processed_tokens.append(token[::-1])
        # Preserve other tokens (punctuation, etc.)
        else:
            processed_tokens.append(token)
    
    # Reconstruct the string
    return ''.join(processed_tokens)