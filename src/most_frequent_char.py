def find_most_frequent_character(string):
    """
    Find the most frequently occurring character in a given string.
    
    Args:
        string (str): The input string to analyze.
    
    Returns:
        str: The most frequently occurring character.
             If multiple characters have the same highest frequency, 
             return the first one in order of appearance.
        None: If the input string is empty.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    if not string:
        return None
    
    # Count character frequencies while preserving order
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    
    # Find the character with maximum frequency
    max_freq = 0
    most_frequent = None
    
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent = char
    
    return most_frequent