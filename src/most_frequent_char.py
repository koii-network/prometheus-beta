def find_most_frequent_char(s: str) -> str:
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
    
    # Count character frequencies
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the character with the maximum frequency
    return max(char_count, key=char_count.get)