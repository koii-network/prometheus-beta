def reverse_word_chars(sentence):
    """
    Take a sentence and return a new sentence with each word's characters reversed.
    
    Args:
        sentence (str): The input sentence to process.
    
    Returns:
        str: A new sentence with characters of each word reversed.
    
    Examples:
        >>> reverse_word_chars("hello world")
        'olleh dlrow'
        >>> reverse_word_chars("Python is awesome")
        'nohtyP si emosewa'
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Split the sentence into words, reverse chars of each word, then join back
    reversed_words = [word[::-1] for word in sentence.split()]
    
    return ' '.join(reversed_words)