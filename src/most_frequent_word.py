def most_frequent_word(text):
    """
    Find the most frequent word in a given string of text.
    
    Args:
        text (str): A string of lowercase words separated by spaces.
    
    Returns:
        str: The most frequently occurring word. 
             If multiple words have the same highest frequency, returns any of them.
    """
    # Handle empty string case
    if not text:
        return ""
    
    # Split the text into words
    words = text.split()
    
    # Count word frequencies using a dictionary
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find the word(s) with maximum frequency
    max_freq = max(word_counts.values())
    
    # Return the first word with maximum frequency
    for word, count in word_counts.items():
        if count == max_freq:
            return word