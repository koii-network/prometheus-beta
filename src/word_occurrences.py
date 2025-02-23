def find_word_occurrences(input_string, target_word):
    """
    Find all occurrences of a target word in a string, 
    with the character position preceding each occurrence.
    
    Args:
        input_string (str): The string to search in
        target_word (str): The word to find
    
    Returns:
        list: A list of tuples with (character_position, occurrence)
    """
    # Validate inputs
    if not isinstance(input_string, str) or not isinstance(target_word, str):
        raise TypeError("Inputs must be strings")
    
    if not input_string or not target_word:
        return []
    
    # Split the input string into words
    words = input_string.split()
    
    # Track occurrences and character positions
    occurrences = []
    current_position = 0
    
    for word in words:
        # Add space length when not first word
        if occurrences:
            current_position += 1
        
        # Check if word matches target word
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Update current position
        current_position += len(word)
    
    return occurrences