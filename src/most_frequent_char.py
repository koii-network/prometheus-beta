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
    
    # Find the max frequency
    max_freq = max(char_count.values())
    
    # Find the first character with the max frequency
    for char, count in char_count.items():
        if count == max_freq:
            return char