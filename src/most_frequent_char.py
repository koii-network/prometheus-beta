def find_most_frequent_character(input_string):
    """
    Find the most frequently occurring character in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             return the first one encountered.
             If the string is empty, return None.
    """
    if not input_string:
        return None
    
    # Create a dictionary to store character frequencies
    char_freq = {}
    
    # Count frequency of each character
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Find the character with the maximum frequency
    max_freq_char = max(char_freq, key=char_freq.get)
    
    return max_freq_char