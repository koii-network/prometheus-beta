def replace_words(text, replacements):
    """
    Perform in-place text replacements using a dictionary of word replacements.
    
    Args:
        text (str): The input text to perform replacements on.
        replacements (dict): A dictionary where keys are words to be replaced 
                             and values are their replacements.
    
    Returns:
        str: The modified text with all specified replacements.
    
    Raises:
        TypeError: If text is not a string or replacements is not a dictionary.
    """
    # Input validation
    if not isinstance(text, str):
        raise TypeError("Input text must be a string")
    
    if not isinstance(replacements, dict):
        raise TypeError("Replacements must be a dictionary")
    
    # Create a sorted list of replacement keys by length (descending)
    # This prevents partial replacements and ensures longer words are replaced first
    sorted_keys = sorted(replacements.keys(), key=len, reverse=True)
    
    # Perform replacements
    for word in sorted_keys:
        # Only replace if the replacement key exists in the dictionary
        if word in text:
            text = text.replace(word, replacements[word])
    
    return text