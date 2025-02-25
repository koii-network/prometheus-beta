def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): A string containing words separated by spaces.
    
    Returns:
        str: The longest word in the sentence. If multiple words have the same 
             maximum length, returns the first occurrence.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If the input string is empty.
    """
    # Type checking
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespaces and handle empty string
    sentence = sentence.strip()
    if not sentence:
        raise ValueError("Input sentence cannot be empty")
    
    # Split the sentence into words and find the longest
    words = sentence.split()
    return max(words, key=len)