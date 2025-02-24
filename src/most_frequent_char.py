def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             returns the first such character encountered.
             Returns None for empty strings.

    Raises:
        TypeError: If input is not a string.
    """
    # Check for invalid input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return None
    
    # Count character frequencies
    char_freq = {}
    for char in input_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Find the character with maximum frequency
    max_freq_char = max(char_freq, key=char_freq.get)
    
    return max_freq_char