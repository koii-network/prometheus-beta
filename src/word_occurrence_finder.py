def find_word_occurrences(text: str, target_word: str) -> list:
    """
    Find all occurrences of a target word in a string, 
    with the character position preceding each occurrence.

    Args:
        text (str): The input string to search in
        target_word (str): The word to find

    Returns:
        list: A list of tuples, each containing the character position 
              and the occurrence of the target word
    """
    # Split the text into words
    words = text.split()
    
    # Store results
    occurrences = []
    
    # Track cumulative character count 
    current_position = 0
    
    # Iterate through words
    for word in words:
        # Check if the current word matches the target
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Calculate the next starting position
        current_position += len(word) + 1
    
    return occurrences