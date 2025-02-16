def alternating_title_case(text: str) -> str:
    """
    Convert a string to alternating title case.
    
    Args:
        text (str): The input string to convert.
    
    Returns:
        str: A string with alternating uppercase and lowercase words.
    
    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Split the string into words
    words = text.split()
    
    # Apply alternating case
    alternating_words = [
        word.upper() if i % 2 == 0 else word.lower() 
        for i, word in enumerate(words)
    ]
    
    # Join the words back together
    return ' '.join(alternating_words)