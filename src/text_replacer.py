def replace_words(text: str, replacements: dict) -> str:
    """
    Perform in-place text replacements based on a dictionary of word replacements.
    
    Args:
        text (str): The input text to perform replacements on
        replacements (dict): A dictionary where keys are words to be replaced 
                             and values are their replacements
    
    Returns:
        str: The modified text with all specified replacements
    
    Raises:
        TypeError: If text is not a string or replacements is not a dictionary
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    
    if not isinstance(replacements, dict):
        raise TypeError("Replacements must be a dictionary")
    
    # Create a copy of the text to perform replacements
    modified_text = text
    
    # Perform replacements
    for old_word, new_word in replacements.items():
        # Ensure both old and new words are strings
        if not isinstance(old_word, str) or not isinstance(new_word, str):
            raise TypeError("All replacement dictionary keys and values must be strings")
        
        # Replace all occurrences of the word
        modified_text = modified_text.replace(old_word, new_word)
    
    return modified_text