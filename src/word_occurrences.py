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
    
    # Track character count and last searched index
    current_char_count = 0
    start_index = 0

    # Continue searching while there are possible matches
    while start_index < len(input_string):
        # Find the next occurrence of the target word
        found_index = input_string.find(target_word, start_index)
        
        # If no more occurrences, break the loop
        if found_index == -1:
            break
        
        # Make sure the word is a complete word (not part of another word)
        is_valid_word = (
            # Check start of string or character before is not alphanumeric
            (found_index == 0 or not input_string[found_index-1].isalnum()) and
            # Check end of string or character after is not alphanumeric
            (found_index + len(target_word) == len(input_string) or 
             not input_string[found_index + len(target_word)].isalnum())
        )
        
        # If it's a valid word occurrence
        if is_valid_word:
            # Find the index in the split string
            words = input_string[:found_index].split()
            
            # Add the occurrence
            occurrences.append((found_index, len(words)))
        
        # Move the start index to continue searching
        start_index = found_index + 1

    return occurrences