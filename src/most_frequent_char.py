def find_most_frequent_char(s: str) -> str:
    """
    Find the most frequently occurring character in a string.
    
    If multiple characters have the same highest frequency, return the first one 
    encountered when reading from left to right.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        str: The most frequent character in the string
    
    Raises:
        ValueError: If the input string is empty
    """
    if not s:
        raise ValueError("Input string cannot be empty")
    
    # Use a dictionary to count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with the maximum frequency
    return max(char_count, key=char_count.get)