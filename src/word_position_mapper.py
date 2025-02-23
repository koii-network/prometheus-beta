def map_word_positions(text):
    """
    Takes a string of text and returns a dictionary mapping unique words to their positions.
    
    Args:
        text (str): Input text to analyze
    
    Returns:
        dict: A dictionary where keys are unique words and values are sorted lists of their positions
    """
    # Split the text into words, converting to lowercase to treat words case-insensitively
    words = text.lower().split()
    
    # Dictionary to store word positions
    word_positions = {}
    
    # Iterate through words and track their positions
    for pos, word in enumerate(words):
        # If word not in dictionary, create a new list
        if word not in word_positions:
            word_positions[word] = []
        
        # Append current position to the word's position list
        word_positions[word].append(pos)
    
    return word_positions