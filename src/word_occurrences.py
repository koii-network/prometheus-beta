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

    # Initialize results
    occurrences = []
    
    # Split the input string into words
    words = input_string.split()
    
    # Track character count
    current_char_count = 0
    
    # Iterate through words with indexes
    for index, word in enumerate(words):
        # Check if current word is the target word
        if word == target_word:
            # Add occurrence with current character count and index
            occurrences.append((current_char_count, index))
        
        # Update character count 
        # Add length of current word and a space 
        # (except for the last word which doesn't have a trailing space)
        if index < len(words) - 1:
            current_char_count += len(word) + 1
        else:
            current_char_count += len(word)

    return occurrences