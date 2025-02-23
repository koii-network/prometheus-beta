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
    
    # Track the longest word and its length
    max_len = 0
    longest_word = None
    
    # Iterate through words to find first longest word 
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
            longest_word = word
    
    return longest_word