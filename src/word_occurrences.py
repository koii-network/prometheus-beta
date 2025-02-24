def find_word_occurrences(input_string: str, target_word: str) -> list:
    """
    Find all occurrences of a target word in a given string, 
    with the character count up to each occurrence.

    Args:
        input_string (str): The string to search in
        target_word (str): The word to find occurrences of

    Returns:
        list: A list of tuples containing (character_count, occurrence_index)
              for each occurrence of the target word

    Raises:
        TypeError: If input_string or target_word is not a string
        ValueError: If input_string or target_word is empty
    """
    # Input validation
    if not isinstance(input_string, str) or not isinstance(target_word, str):
        raise TypeError("Both input_string and target_word must be strings")
    
    if not input_string or not target_word:
        raise ValueError("Input string and target word cannot be empty")

    # Split the input string into words
    words = input_string.split()
    
    # Initialize results and tracking variables
    occurrences = []
    current_char_count = 0

    # Iterate through words to find occurrences
    for index, word in enumerate(words):
        # Add word length and space (except for first word)
        if index > 0:
            current_char_count += len(words[index-1]) + 1  # +1 for space
        
        # Check if current word matches target word
        if word == target_word:
            occurrences.append((current_char_count, index))

    return occurrences