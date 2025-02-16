def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a given string.
    
    Args:
        text (str): The input string to be capitalized.
    
    Returns:
        str: A string with the first letter of each word capitalized.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return ""
    
    # Capitalize first letter of each word
    return ' '.join(word.capitalize() for word in text.split())