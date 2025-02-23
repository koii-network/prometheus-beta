def most_frequent_word(text: str) -> str:
    """
    Find the most frequently occurring word in the input text.

    Args:
        text (str): A string of lowercase letters separated by spaces.

    Returns:
        str: The most frequently occurring word in the text.
             If multiple words have the same highest frequency, 
             returns any of those words.

    Raises:
        ValueError: If the input text is empty or contains invalid characters.
    """
    # Check for empty input
    if not text:
        raise ValueError("Input text cannot be empty")
    
    # Validate input (only lowercase letters and spaces)
    if not all(char.islower() or char.isspace() for char in text):
        raise ValueError("Input must contain only lowercase letters and spaces")
    
    # Split the text into words
    words = text.split()
    
    # If no words, raise an error
    if not words:
        raise ValueError("Input text contains no words")
    
    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find the most frequent word
    return max(word_counts, key=word_counts.get)