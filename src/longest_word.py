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
    
    # Split the sentence into words and find the longest
    words = sentence.split()
    longest = max(words, key=len)
    
    # From the words with the max length, find the one that appears first
    max_len = len(longest)
    return [word for word in words if len(word) == max_len][0]