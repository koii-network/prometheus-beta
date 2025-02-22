def find_most_frequent_char(s):
    """
    Find the most frequently occurring character in a string.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        str: The most frequently occurring character
        
    Raises:
        ValueError: If the input string is empty
    """
    if not s:
        raise ValueError("Input string cannot be empty")
    
    # Count occurrences of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the character with maximum count
    return max(char_counts, key=char_counts.get)