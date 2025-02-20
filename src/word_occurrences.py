def find_word_occurrences(text: str, target_word: str) -> list:
    """
    Find all occurrences of a target word in a string with their character positions.
    
    Args:
        text (str): The input text to search in.
        target_word (str): The word to find occurrences of.
    
    Returns:
        list: A list of tuples containing (character_position, word) for each occurrence.
    """
    # Validate inputs
    if not isinstance(text, str) or not isinstance(target_word, str):
        raise TypeError("Both text and target_word must be strings")
    
    if not text or not target_word:
        return []
    
    # Split the text into words
    words = text.split()
    
    # Track occurrences and character positions
    occurrences = []
    current_position = 0
    
    for word in words:
        # Check if the current word matches the target word
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Update current position (add word length and a space)
        current_position += len(word) + 1
    
    return occurrences