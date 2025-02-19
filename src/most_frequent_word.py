def most_frequent_word(text):
    """
    Find the most frequently occurring word in the input text.
    
    Args:
        text (str): A string of lowercase words separated by spaces.
    
    Returns:
        str: The most frequently occurring word.
    """
    # If the input is empty, return an empty string
    if not text:
        return ""
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find the most frequent word
    return max(word_counts, key=word_counts.get)