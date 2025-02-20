def track_word_positions(text):
    """
    Takes a string of text as input and returns a dictionary 
    where keys are unique words and values are lists of their positions.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        dict: Dictionary with words as keys and their positions as sorted lists
    """
    # Remove leading/trailing whitespace and convert to lowercase for consistency
    text = text.strip().lower()
    
    # Split the text into words
    words = text.split()
    
    # Dictionary to store word positions
    word_positions = {}
    
    # Track positions of each word
    for position, word in enumerate(words):
        # If word is not in dictionary, create a new list
        if word not in word_positions:
            word_positions[word] = []
        
        # Append current position to the word's position list
        word_positions[word].append(position)
    
    return word_positions