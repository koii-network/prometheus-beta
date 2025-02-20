def find_word_occurrences(input_string, target_word):
    """
    Find all occurrences of a target word in a string, with their character positions.
    
    Args:
        input_string (str): The string to search in
        target_word (str): The word to find
    
    Returns:
        list: A list of tuples, each containing the character position and the occurrence
    """
    # Validate inputs
    if not isinstance(input_string, str) or not isinstance(target_word, str):
        raise TypeError("Both input_string and target_word must be strings")
    
    if not input_string or not target_word:
        return []
    
    # Split the input string into words
    words = input_string.split()
    
    # Track results and position
    occurrences = []
    current_position = 0
    
    for word in words:
        # Add current word length plus a space (except for the first word)
        if current_position > 0:
            current_position += 1  # Add space
        
        # Check if current word matches target word
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Update current position
        current_position += len(word)
    
    return occurrences