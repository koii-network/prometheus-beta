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
    
    def split_complex_string(s):
        """
        Intelligently split a complex string while preserving palindrome tokens.
        Separates numeric, letter, and special tokens while keeping palindromes whole.
        """
        import re
        
        # First, identify palindrome tokens that should remain unchanged
        palindrome_tokens = [token for token in re.findall(r'\w+', s) if is_palindrome(token)]
        
        # If a palindrome exists in the string, we need a special splitting approach
        if palindrome_tokens:
            # Find the first palindrome
            first_palindrome = palindrome_tokens[0]
            parts = s.split(first_palindrome)
            
            result = []
            for i, part in enumerate(parts):
                # Process non-palindrome parts
                if part:
                    result.extend(split_simple_string(part))
                
                # Add palindrome between parts if not the last iteration
                if i < len(parts) - 1:
                    result.append(first_palindrome)
            
            return result
        
        # If no palindromes, use simple splitting
        return split_simple_string(s)
    
    def split_simple_string(s):
        """Split a string into numeric, letter, and other tokens."""
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
    tokens = split_complex_string(input_string)
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
        # Preserve other tokens (punctuation, mixed, etc.)
        else:
            processed_tokens.append(token)
    
    # Reconstruct the string
    return ''.join(processed_tokens)