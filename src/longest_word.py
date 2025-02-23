def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words 
             have the same maximum length, returns the first occurrence.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the input sentence is empty or contains only whitespace.
    """
    # Validate input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and check if empty
    cleaned_sentence = sentence.strip()
    if not cleaned_sentence:
        raise ValueError("Sentence cannot be empty")
    
    # Split the sentence into words
    words = cleaned_sentence.split()
    
    # If no words found, raise ValueError
    if not words:
        raise ValueError("No words found in the sentence")
    
    # Find and return the longest word
    return max(words, key=len)