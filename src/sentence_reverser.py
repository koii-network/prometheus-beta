def reverse_words_in_sentence(sentence):
    """
    Takes a sentence and returns a new sentence with each word reversed in character order.
    
    Args:
        sentence (str): The input sentence to be processed.
    
    Returns:
        str: A new sentence with each word's characters reversed.
    
    Example:
        >>> reverse_words_in_sentence("Hello World")
        'olleH dlroW'
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    if not sentence:
        return ""
    
    # Split the sentence into words and reverse each word
    reversed_words = [word[::-1] for word in sentence.split()]
    
    # Join the reversed words back into a sentence
    return " ".join(reversed_words)