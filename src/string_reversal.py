def reverse_string(input_string):
    """
    Reverse a given string, preserving word order and special characters.
    
    Args:
        input_string (str): The string to be reversed.
    
    Returns:
        str: The reversed string.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Reverse each word while preserving special characters
    reversed_words = []
    for word in words:
        # Separate alphanumeric characters
        alpha_chars = [char for char in word if char.isalnum()]
        
        # Reverse only the alphanumeric characters
        reversed_alpha = alpha_chars[::-1]
        
        # Reconstruct the word with original special character positions
        reversed_word = []
        alpha_index = 0
        for char in word:
            if char.isalnum():
                # Replace with reversed alphanumeric character
                reversed_word.append(reversed_alpha[alpha_index])
                alpha_index += 1
            else:
                # Keep special characters in their original position
                reversed_word.append(char)
        
        reversed_words.append(''.join(reversed_word))
    
    # Return the reversed string, maintaining original word order
    return ' '.join(reversed_words[::-1])