import re

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
    
    # Find all occurrences of the word
    for match in re.finditer(r'\b' + re.escape(target_word) + r'\b', input_string):
        # Get the start index of the match
        match_start = match.start()
        
        # Find the number of words before this match
        words_before = len(re.findall(r'\S+', input_string[:match_start]))
        
        # Add to occurrences
        occurrences.append((match_start, words_before))

    return occurrences