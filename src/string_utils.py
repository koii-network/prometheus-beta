def reverse_words(input_string: str) -> str:
    """
    Reverse the order of words in a given string, handling multiple spaces 
    and ignoring non-alphabetic characters.
    
    Args:
        input_string (str): The input string to be processed
    
    Returns:
        str: A string with words reversed, preserving original spacing and 
             non-alphabetic characters
    
    Examples:
        >>> reverse_words("Hello World")
        'World Hello'
        >>> reverse_words("  Hello   World  ")
        '  World   Hello  '
        >>> reverse_words("Hello123 World456")
        'World456 Hello123'
    """
    # Handle edge cases
    if not input_string or not isinstance(input_string, str):
        return input_string
    
    # Split the string preserving whitespace
    parts = []
    current_word = []
    current_space = []
    
    for char in input_string:
        if char.isspace():
            # If we have a word in progress, add it to parts
            if current_word:
                parts.append(''.join(current_word))
                current_word = []
            current_space.append(char)
        else:
            # If we have spaces in progress, add them before the word
            if current_space:
                parts.append(''.join(current_space))
                current_space = []
            current_word.append(char)
    
    # Add any remaining word or space
    if current_word:
        parts.append(''.join(current_word))
    if current_space:
        parts.append(''.join(current_space))
    
    # Reverse the parts
    return ''.join(reversed(parts))