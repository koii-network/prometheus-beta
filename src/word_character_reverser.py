def reverse_word_characters(sentence: str) -> str:
    """
    Reverses the characters of each word in a given sentence while maintaining 
    the original word order.

    Args:
        sentence (str): The input sentence to process.

    Returns:
        str: A new sentence with characters of each word reversed.

    Examples:
        >>> reverse_word_characters("hello world")
        'olleh dlrow'
        >>> reverse_word_characters("Python is awesome")
        'nohtyP si emosewa'
        >>> reverse_word_characters("")
        ''
    """
    # Handle empty string case
    if not sentence:
        return ""
    
    # Split the sentence into words and reverse characters of each word
    reversed_words = [word[::-1] for word in sentence.split()]
    
    # Rejoin the words back into a sentence
    return " ".join(reversed_words)