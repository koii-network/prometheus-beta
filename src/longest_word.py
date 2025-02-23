def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to analyze.

    Returns:
        str: The longest word in the sentence. If multiple words 
             have the same maximum length, returns the first occurrence.
        
    Raises:
        TypeError: If input is not a string.
        ValueError: If the input string is empty or contains only whitespace.

    Examples:
        >>> find_longest_word("The quick brown fox jumps over the lazy dog")
        'quick'
        >>> find_longest_word("Python is awesome")
        'awesome'
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and handle empty string
    sentence = sentence.strip()
    if not sentence:
        raise ValueError("Input sentence cannot be empty")
    
    # Split the sentence into words 
    words = sentence.split()
    
    # Find the max length while preserving first occurrence order
    max_length = 0
    longest_word = None
    
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            max_length = word_length
            longest_word = word
    
    return longest_word