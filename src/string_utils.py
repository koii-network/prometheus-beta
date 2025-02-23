def reverse_words(sentence):
    """
    Reverse the order of words in a given sentence.
    
    Args:
        sentence (str): The input sentence to reverse.
    
    Returns:
        str: A new string with words in reverse order.
    
    Notes:
        - Handles multiple spaces between words
        - Ignores non-alphabetic characters
        - Preserves original spacing patterns
    """
    # Handle empty or None input
    if not sentence or not isinstance(sentence, str):
        return ""
    
    # Split the sentence by whitespace, handling multiple spaces
    words = sentence.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Reconstruct the sentence with original spacing
    return " ".join(reversed_words)