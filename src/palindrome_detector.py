def contains_palindrome_word(input_string):
    """
    Determine if the input string contains a palindrome word.
    
    Args:
        input_string (str): A string containing words, numbers, and special characters
    
    Returns:
        bool: True if the string contains a palindrome word, False otherwise
    """
    # Remove special characters and split into words
    import re
    
    # Clean the string: remove special characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string.lower())
    
    # Split into words
    words = cleaned_string.split()
    
    # Check each word for palindrome
    for word in words:
        # Remove any numbers from the word
        word = ''.join(char for char in word if char.isalpha())
        
        # Skip empty strings
        if not word:
            continue
        
        # Check if word is a palindrome
        if word == word[::-1] and len(word) > 1:
            return True
    
    return False