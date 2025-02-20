def map_word_positions(text):
    """
    Map words to their positions in the input text.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        dict: A dictionary with unique words as keys and lists of their positions as values
    """
    # Split the text into words and preserve their original case
    words = text.split()
    
    # Create a dictionary to store word positions
    word_positions = {}
    
    # Iterate through words and track their positions
    for position, word in enumerate(words):
        # Convert word to lowercase for case-insensitive unique key
        normalized_word = word.lower()
        
        # Add position to the word's list of positions
        if normalized_word not in word_positions:
            word_positions[normalized_word] = []
        word_positions[normalized_word].append(position)
    
    return word_positions