def reverse_sentence_words(sentence):
    """
    Reverses the characters of each word in a sentence while maintaining the word order.
    
    Args:
        sentence (str): The input sentence to be processed.
    
    Returns:
        str: A new sentence with each word's characters reversed.
    
    Examples:
        >>> reverse_sentence_words("hello world")
        'olleh dlrow'
        >>> reverse_sentence_words("Python is awesome")
        'nohtyP si emosewa'
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    if not sentence:
        return ""
    
    # Split the sentence into words, reverse each word, then join back
    reversed_words = [word[::-1] for word in sentence.split()]
    return " ".join(reversed_words)