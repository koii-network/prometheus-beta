def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): The input sentence to search for the longest word.
    
    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, return the first one encountered.
    
    Raises:
        ValueError: If the input is not a string or is an empty string.
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    # Remove leading/trailing whitespace and split the sentence
    words = sentence.strip().split()
    
    # Check for empty sentence
    if not words:
        raise ValueError("Input sentence is empty")
    
    # Find the longest word
    return max(words, key=len)