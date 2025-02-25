import re

def reverse_word_characters(sentence: str) -> str:
    """
    Reverses the characters of each word in a given sentence while maintaining 
    the original word order and preserving punctuation.

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
        >>> reverse_word_characters("hello, world!")
        'olleh, dlrow!'
        >>> reverse_word_characters("python 3.9 rocks")
        'nohtyp 9.3 skcor'
    """
    # Handle empty string case
    if not sentence:
        return ""
    
    # Function to reverse a word while preserving its punctuation and numeric formatting
    def reverse_word_with_punctuation(word):
        # Separate the word from its punctuation and numeric formatting
        match = re.match(r'^(\W*)([^\W\d]*\d*[^\W\d]*)(\d*)([\W]*)$', word)
        if not match:
            return word
        
        # Unpack the groups: leading punct, alphanumeric core, numeric part, trailing punct
        pre_punct, letter_part, numeric_part, post_punct = match.groups()
        
        # Reverse the alphanumeric part and reassemble with punctuation and numeric part
        return pre_punct + letter_part[::-1] + numeric_part + post_punct
    
    # Split the sentence into words, reverse each, then rejoin
    reversed_words = [reverse_word_with_punctuation(word) for word in sentence.split()]
    
    return " ".join(reversed_words)