def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. 
             If multiple words have the same maximum length, returns the first one.
             If the sentence is empty or contains no words, returns an empty string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Strip leading/trailing whitespace and split into words
    words = sentence.strip().split()
    
    # If no words, return empty string
    if not words:
        return ""
    
    # Find the longest word 
    return max(words, key=len)