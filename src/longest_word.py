def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first occurrence.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty or contains only whitespace.
    """
    # Validate input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and split into words
    words = sentence.strip().split()
    
    # Check for empty input after stripping
    if not words:
        raise ValueError("Input sentence cannot be empty")
    
    # Find the longest word
    return max(words, key=len)