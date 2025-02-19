def to_camel_case(text):
    """
    Convert a string to camel case.
    
    Handles different input formats:
    - Space-separated words
    - Hyphen-separated words
    - Underscore-separated words
    
    Args:
        text (str): Input string to convert to camel case
    
    Returns:
        str: Camel case version of the input string
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return empty string
    if not text:
        return ""
    
    # Replace separators with spaces, then split
    words = text.replace('-', ' ').replace('_', ' ').split()
    
    # First word is always lowercase
    camel_words = [words[0].lower()]
    
    # Capitalize first letter of subsequent words
    camel_words.extend(word.capitalize() for word in words[1:])
    
    return ''.join(camel_words)