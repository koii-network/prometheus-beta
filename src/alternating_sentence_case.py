def alternating_sentence_case(text):
    """
    Convert a string to alternating sentence case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating sentence case.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # If the string is empty, return empty string
    if not text:
        return ""
    
    # Split the text into words
    words = text.split()
    
    # Convert words to alternating case
    alternating_words = [
        word.capitalize() if i % 2 == 0 else word.lower() 
        for i, word in enumerate(words)
    ]
    
    # Join the words back together
    return " ".join(alternating_words)