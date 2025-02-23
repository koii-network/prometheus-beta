import re

def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. If multiple words 
             have the same maximum length, returns the first occurrence.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the input sentence is empty or contains only whitespace.
    """
    # Validate input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove leading/trailing whitespace and check if empty
    cleaned_sentence = sentence.strip()
    if not cleaned_sentence:
        raise ValueError("Sentence cannot be empty")
    
    # Remove punctuation and split into words
    # Keep words as-is for first occurrence priority
    words_with_punct = cleaned_sentence.split()
    words = [re.sub(r'[^\w\s]', '', word) for word in words_with_punct]
    
    # If no words found, raise ValueError
    if not words:
        raise ValueError("No words found in the sentence")
    
    # Find the length of the longest word
    max_length = len(max(words, key=len))
    
    # Find the first word with the maximum length
    for word, orig_word in zip(words, words_with_punct):
        if len(word) == max_length:
            return orig_word