def to_header_case(text: str) -> str:
    """
    Convert a string to header case (capitalized words with no separators).
    
    Args:
        text (str): Input string to convert
    
    Returns:
        str: String converted to header case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not text:
        return ""
    
    # Split the string by various possible separators
    words = []
    current_word = ""
    for char in text:
        if char in [' ', '_', '-']:
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    
    # Add the last word
    if current_word:
        words.append(current_word)
    
    # Capitalize or preserve existing capitalization
    def capitalize_word(word):
        if word[0].isupper():
            return word
        return word.capitalize()
    
    # Capitalize each word and join
    return ''.join(capitalize_word(word) for word in words)