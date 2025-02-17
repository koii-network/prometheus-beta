def find_most_frequent_character(s):
    """
    Find the most frequently occurring character in a string.
    
    Args:
        s (str): The input string to analyze.
    
    Returns:
        str: The most frequently occurring character.
             If multiple characters have the same highest frequency, 
             return the first one encountered.
             If the string is empty, return None.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return None
    
    # Count character frequencies
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the character with max frequency
    return max(char_counts, key=char_counts.get)