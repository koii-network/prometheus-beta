def find_word_occurrences(input_string, target_word):
    """
    Find all occurrences of a target word in a given string, 
    with the character index of each occurrence.

    Args:
        input_string (str): The string to search in
        target_word (str): The word to find occurrences of

    Returns:
        list: A list of tuples containing (char_index, occurrence)
               where char_index is the total number of characters 
               up to the start of the occurrence

    Raises:
        TypeError: If input_string or target_word is not a string
        ValueError: If target_word is an empty string
    """
    # Validate inputs
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    if not isinstance(target_word, str):
        raise TypeError("target_word must be a string")
    if not target_word:
        raise ValueError("target_word cannot be an empty string")

    # Initialize results list and tracking variables
    occurrences = []
    words = input_string.split()
    current_char_index = 0

    # Iterate through words to find matches and track character index
    for word in words:
        # Check if current word matches target
        if word == target_word:
            occurrences.append((current_char_index, word))
        
        # Update character index (add word length + space, except for last word)
        current_char_index += len(word) + 1

    return occurrences