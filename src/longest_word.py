def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): The input sentence to search for the longest word.
    
    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first occurrence.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If the input sentence is empty or contains only whitespace.
    """
    # Check input type
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and check if sentence is empty
    sentence = sentence.strip()
    if not sentence:
        raise ValueError("Sentence cannot be empty")
    
    # Split the sentence into words
    words = sentence.split()
    
    # Find the longest word
    return max(words, key=len)