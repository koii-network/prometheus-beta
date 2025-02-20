def track_word_positions(text):
    """
    Takes a string of text and returns a dictionary of words with their positions.
    
    Args:
        text (str): Input text to analyze.
    
    Returns:
        dict: A dictionary where keys are unique words and values are sorted lists of their positions.
    
    Example:
        >>> track_word_positions("hello world hello")
        {'hello': [0, 2], 'world': [1]}
    """
    # Split the text into words and remove any leading/trailing whitespace
    words = text.split()
    
    # Create a dictionary to store word positions
    word_positions = {}
    
    # Iterate through words and track their positions
    for position, word in enumerate(words):
        # Normalize the word by converting to lowercase
        normalized_word = word.lower()
        
        # Add the position to the word's list of positions
        if normalized_word not in word_positions:
            word_positions[normalized_word] = [position]
        else:
            word_positions[normalized_word].append(position)
    
    return word_positions