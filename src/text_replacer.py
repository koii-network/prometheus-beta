def replace_words(text: str, replacements: dict) -> str:
    """
    Perform in-place text replacements using a dictionary of word replacements.

    Args:
        text (str): The input text to be modified.
        replacements (dict): A dictionary where keys are words to be replaced 
                             and values are their replacements.

    Returns:
        str: The modified text with specified word replacements.

    Examples:
        >>> replace_words("hello world", {"hello": "hi", "world": "earth"})
        'hi earth'
        >>> replace_words("the quick brown fox", {"quick": "lazy"})
        'the lazy brown fox'
    """
    # Handle edge cases
    if not text or not replacements:
        return text

    # Split the text into words
    words = text.split()
    
    # Replace words
    replaced_words = [
        replacements.get(word, word) for word in words
    ]
    
    # Reconstruct the text
    return ' '.join(replaced_words)